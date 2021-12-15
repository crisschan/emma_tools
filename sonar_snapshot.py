#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   sonar_snapshot.py
@Time    :   2021/12/14 14:27:42
@Author  :   CrissChan 
@Version :   1.0
@Site    :   https://blog.csdn.net/crisschan
@Desc    :   for the sonarqube's Measures
'''

# here put the import lib

import requests
from requests.models import HTTPBasicAuth
import json

class SonarSnapshot(object):
    def __init__(self,usrname,pwd,sonar_uri) -> None:
        super().__init__()
        # self.usrname = usrname
        # self.pwd = pwd
        self.auth = HTTPBasicAuth(usrname,pwd)
        self.sonar_uri = sonar_uri
        
        # self.sonar_authon = self.sonar_uri+'/api/authentication/login'
   
    def get_issues(self,componentskey,types='BUG,VULNERABILITY'):
        '''
        des 查询指定项目的 issues
        params：
            componentskey：查询的项目
            types：CODE_SMELL，BUG，VULNERABILITY 一个或者多个，多个用英文都号分割。
        '''
        issue_url =  self.sonar_uri+'/api/issues/search?componentKeys='+componentskey+'&types='+types
        res = requests.get(issue_url,auth = self.auth)
        res_json = json.loads(res.text)
        page_size= res_json['paging']['pageSize']
        total= res_json['paging']['total']
        page_count = total/page_size+1
        page_number = 0
        issue_list=[]
        while page_number<page_count:
            purl = issue_url+'&p='+str(page_number+1)
            res_issue = requests.get(purl,auth = self.auth)
            # print(res_issue.text)
            issue_list=issue_list+json.loads(res_issue.text)['issues']
            page_number=page_number+1
        return (issue_list)

        # return res_json
        
    def get_measures(self,componentskey,metirc_keys='alert_status,bugs,reliability_rating,vulnerabilities,security_rating,code_smells,sqale_rating,duplicated_lines_density,coverage,ncloc,ncloc_language_distribution,complexity'):
        '''
        des 查询指定项目的metrics
        params:
            componentskey：查询的项目
            metirc_keys：度量结果
        return: 
            项目当前的度量metrics，json格式
        '''
   
        measure_url = self.sonar_uri+'/api/measures/component?component='+componentskey+'&metricKeys='+metirc_keys
        res = requests.get(measure_url,auth = self.auth)
        res_json = json.loads(res.text)
        return res_json

    def get_projects(self):
        '''
        按照一页100条的默认参数分页
        return 如下结构的list
        {
		"key": componentskey也是projectkey,
		"name":项目名称,
		"qualifier":TRK - for projects；APP - for applications
		"isFavorite": 是否收藏,
		"analysisDate": 最近一次分析时间
		"tags": [],
		"visibility": "public",
		"needIssueSync": false
	
        '''
        projects_url = self.sonar_uri+'/api/components/search_projects'
        res = requests.get(projects_url,auth = self.auth)
        res_json = json.loads(res.text)
        page_size= res_json['paging']['pageSize']
        total= res_json['paging']['total']
        page_count = total/page_size+1
        page_number = 0
        project_list=[]
        while page_number<page_count:
            purl = projects_url+'?p='+str(page_number+1)
            res_projects = requests.get(purl,auth = self.auth)
            project_list=project_list+json.loads(res_projects.text)['components']
            page_number=page_number+1
        return (project_list)

# if __name__ == '__main__':
#     ss = SonarSnapshot('chenlei','cde3xsw2zaq1','http://10.51.129.18:9000')
#     # pl= ss.get_projects()
#     # fw = open('t.txt','w')
#     # # lists = ss.get_issues('com.alibaba.intl.sourcing.test:1001237_java_HedgingAS',types='CODE_SMELL')
#     # # print(len(lists))
#     # fw.write(json.dumps(lists))
#     # fw.flush()
#     # fw.close()
   