import os
from urllib.parse import urlparse
import sys
from accio import  parse_tools
import re

class locust_template(object):
    def __init__(self):
        # self.root_path = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
        self.root_path = os.path.dirname(os.path.join(os.getcwd()))

    def creat_dir(self):
        if not os.path.exists(self.root_path + '\\Performance'):
            os.makedirs(self.root_path + '\\Performance')

    def creat_template(self,root):
        file_path = self.root_path + "\\TestCase\\"
        f_list = os.listdir(file_path)
        self.creat_dir()
        test_case_file=parse_tools.Parse.find_casefile(file_path,f_list)
        r = ""
        file_list = []
        if len(test_case_file):
                for i in test_case_file:
                    file = file_path + str(i)
                    # print(file)
                    with open(file, encoding='utf-8') as outfile:
                        contents_str = outfile.read()
                        # print(file)
                        # 查找/开头" 结尾的任意字符串
                        convert_source = re.findall(r'/.*"', contents_str)
                        list_key_dict=parse_tools.Parse.extract_key(contents_str)
                        # list_key_dict=eval(list_key[0].replace(': ', ': "').replace(',', '",').replace('}', '"}'))
                        re_str=""
                        jshu=0
                        for yy in list_key_dict.keys():
                             re_str= re_str+"\""+yy+"\""+":out["+str(jshu)+"][count]"+","+"\r\n\t\t"
                             jshu +=1
                        #去掉最后一个逗号
                        re_str=re_str[:-5]
                        url = str(convert_source[0].replace('"', ""))
                        parse_url = urlparse(url)
                        url_path = parse_url.path
                        dir_path = parse_tools.Parse.path(url)
                        dir = root + '\\Performance\\{a}_locustfile.py'.format(a=dir_path)
                        if contents_str.find('request.post') != -1:
                            method = 'post'
                            body='data'
                        elif contents_str.find('request.get') != -1:
                            method = 'get'
                            body='params'
                        elif contents_str.find('request.put') != -1:
                            method = 'put'
                            body = 'data'
                        else:
                            raise Exception("该reques请求方式不是get\put\post")
                            sys.exit()
                    locustfile_templater = '''from locust import HttpUser, TaskSet, task,between
from accio import locust_read_parameterfile 
import os
import  json
import queue
from operator import itemgetter
#一次加载数据到队列
def queue_data():
    queue_data = queue.Queue()  # 默认为先进先出  该队列为task_set共享
    # queue.LifoQueue(),后进先出
    new_dict = locust_read_parameterfile.file_analysis.creatparm("loadfile.xlsx")
    key_list=[]
    count=0
    for k,v in new_dict.items():
        key_list.append(k)
    #一次读入多列值
    out = itemgetter(*key_list)(new_dict)
    max_len=0
    for i in out:
        if max_len< len(i):
            max_len=len(i)

    for i  in  range(max_len):
        params = {
         #取第一列的值 
        %s
        }
        count +=1
        queue_data.put_nowait(params)  # put_nowait 不阻塞
    return queue_data

def profile(self):
            # get_nowait() 取不到数据直接崩溃；get() 取不到数据会一直等待
            try:
                data=self.user.queue_data_test.get_nowait()
            except queue.Empty:  # 取不到数据时，走这里
                print('数据跑完了，任务结束')
                exit(0)
            params = json.dumps(data,ensure_ascii=False)            
            headers={}  
            with self.client.%s(url='%s', %s=params,headers=headers, catch_response=True) as response:
                if "success"in response.text:
                    response.success()
                else:
                    response.failure(response.text)
            self.user.queue_data_test.put_nowait(data)  # 把取出来的数据重新加入队列

class locustfile(TaskSet):
        def on_start(self):
            # 虚拟用户启动Task时运行
            print('虚拟用户启动Task时运行start')

        def on_stop(self):
            # 虚拟用户结束Task时运行
            print('虚拟用户结束Task时运行end')
        #压测接口，设置权重值，默认为1，值越大，优先执行
        tasks = {profile: 1}

class WebsiteUser(HttpUser):
        host = "http://gw.enncloud.cn/"
        tasks = [locustfile]
        #调用队列方法
        queue_data_test = queue_data()
        # 单位为秒
        wait_time = between(5, 6)
'''%(re_str,method,url_path,body)
                    wf = locustfile_templater
                    with open(dir, 'w', encoding="utf-8") as outfile:
                        outfile.write(str(wf))
        else:
            print('请确认TestCase文件夹下是否存在test 前缀文件！')
            sys.exit()

# if __name__ == '__main__':
#     l=locust_template()
#     ll=l.root_path
#     l.creat_template(ll)