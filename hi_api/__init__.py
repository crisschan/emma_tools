from httper import Httper

hper = Httper('http://www.baidu.com')
res = hper.get('/')
print(res.text)