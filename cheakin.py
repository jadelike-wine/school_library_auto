import requests
import json
from requests.packages import urllib3
import http.cookiejar
import time
import datetime
import re


urllib3.disable_warnings()

def login(no,pd,seats,starttime):
	while True:
		try:
			#print(duration)
			url = 'https://hdu.huitu.zhishulib.com/User/Index/login?LAB_JSON=1'
			global s
			s = requests.session()
			s.headers['Accept-Language'] = 'zh-Hans-CN, zh-Hans; q=0.5'
			s.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
			r = s.get(url, verify=False).text
			code = json.loads(r)['content']['data']['code']
			sstr = json.loads(r)['content']['data']['str']
			r = s.post(url ='https://hdu.huitu.zhishulib.com/api/1/login',json = {'login_name' : no,'password' : pd,'code':code,'str':sstr,"org_id": "104",
		"login_name_type": "school_number",
		"_ApplicationId": "lab4",
		"_JavaScriptKey": "lab4",
		"_ClientVersion": "js_xxx",
		"_InstallationId": "98707b96-bdd3-aa6e-b360-5293d12cc718"}).text
			#print(r)
			objectId = json.loads(r)['objectId']
			c = requests.cookies.RequestsCookieJar()
			c.set('cookie-name','cookie-value')
			s.cookies.update(c)
			r = s.get(url = 'https://hdu.huitu.zhishulib.com/Space/Category/list?LAB_JSON=1').text
			result = json.loads(r)['content']['children'][0]['link']['data']['url']
			f1=re.findall('(\d+)',result)[0]
			urll = 'https://hdu.huitu.zhishulib.com/Seat/Index/checkIn?LAB_JSON=1&bookingId='+f1
			r = s.post(url = urll).text
			#print(r)
			if(json.loads(r)['DATA']['result'] == 'fail'):
				print('fail')
				#r = requests.get('https://sc.ftqq.com/SCU25960T2f6da6da1de67736b6b96186dcbd422b5aeda5af30aaa.send?text=座位签到失败&desp='+str(time.time()))
			else:
				print('success')
				#r = requests.get('https://sc.ftqq.com/SCU25960T2f6da6da1de67736b6b96186dcbd422b5aeda5af30aaa.send?text=座位签到成功&desp='+str(time.time()))
			break
		except Exception as e:
			print(no+'have a problem')
			break


if __name__ == '__main__':
	login('18071122','lyp123456','29074',9)
	'''
	login('16222555','Hdu1091717','10326',9)
	login('16151226','16151226','10328',9)
	login('16221626','16221626','10325',9)
	login('17052241','17052241','10327',9)
	login('16151232','16151232','28997',9)
	login('16120102','16120102','28997',9)
	'''
