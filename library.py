import requests
import json
from requests.packages import urllib3
import http.cookiejar
import time
import datetime


urllib3.disable_warnings()

def login(no,pd,seats,starttime,week):
		#time.sleep(4)
	timehour = time.localtime(time.time()).tm_hour
	timemins = time.localtime(time.time()).tm_min
	today = datetime.date.today()
	tomorrow = today + datetime.timedelta(days=2)
	tomorrow_start_time = int(time.mktime(time.strptime(str(tomorrow), '%Y-%m-%d')))
	tomorrow_start_time += 3600*starttime
	duration = 79200 - 3600*starttime
	#print(duration)
	today = datetime.date.today()
	twoday = today + datetime.timedelta(days=2)
	twoday = twoday.isoweekday()
	if twoday in week:
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
		r = s.post(url = 'https://hdu.huitu.zhishulib.com/Seat/Index/bookSeats?LAB_JSON=1',data = {'beginTime'	:tomorrow_start_time,'duration':	duration,'seats[0]':	seats,'seatBookers[0]':	objectId}).text
		#print(r)
		result = json.loads(r)['DATA']['result']
		print(result)
		if (result == 'success'):
			print('预定成功\n')
		elif(result == 'fail'):
			r = requests.get('https://sc.ftqq.com/SCU25960T2f6da6da1de67736b6b96186dcbd422b5aeda5af30aaa.send?text=座位预定失败&desp='+str(time.time()))
	else:
		print('不在规定时间')

if __name__ == '__main__':
	login('18071122','lyp123456','29074',9,[1,2,3,4,5,6,7])
	'''
	login('16222555','Hdu1091717','10326',9,[1,2,3,4,5,6,7])
	login('16151226','16151226','10328',9,[1,2,3,4,5,6,7])
	login('16221626','16221626','10325',9,[1,2,3,4,5,6,7])
	login('17052241','17052241','10327',9,[1,2,3,4,5,6,7])
	login('16151232','16151232','28997',9,[1,2,3,4,5,6,7])

	login('16120102','16120102','10332',8,[1,2,6,7])
	login('16120102','16120102','10332',15,[3,4,5])
	login('16120106','16120106','10330',8,[1,2,6,7])
	login('16120106','16120106','10330',15,[3,4,5])
	login('16120107','16120107','10331',8,[1,2,6,7])
	login('16120107','16120107','10331',15,[3,4,5])
	'''