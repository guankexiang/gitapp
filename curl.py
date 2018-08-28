#-*- coding: UTF-8 -*-
import os,sys
import time
import sys
import pycurl
import json

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

class joincontents:
	def __init__(self):
		self.contents = ''
	def callback(self,curl):
		self.contents = self.contents + curl.decode('UTF-8')

def curlurl(url):
	t = joincontents()
	c = pycurl.Curl()
	c.setopt(pycurl.WRITEFUNCTION,t.callback)
	c.setopt(pycurl.ENCODING,'gzip')
	c.setopt(pycurl.URL,url)

	c.perform()
	# NAMELOOKUP_TIME = c.getinfo(c.NAMELOOKUP_TIME)
	# CONNECT_TIME = c.getinfo(c.CONNECT_TIME)
	# PRETRANSFER_TIME = c.getinfo(c.PRETRANSFER_TIME)
	# STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME)
	# TOTAL_TIME = c.getinfo(c.TOTAL_TIME)
	# HTTP_CODE = c.getinfo(c.HTTP_CODE)
	# SIZE_DOWNLOAD = c.getinfo(c.SIZE_DOWNLOAD)
	# HEADER_SIZE = c.getinfo(c.HEADER_SIZE)
	# SPEED_DOWNLOAD = c.getinfo(c.SPEED_DOWNLOAD)

	# print("HTTP状态码：%s" %(HTTP_CODE))
	# print("DNS解析时间：%.2f ms" %(NAMELOOKUP_TIME*1000))
	# print("建立连接时间：%.2f ms" %(CONNECT_TIME*1000))
	# print("准备传输时间：%.2f ms" %(PRETRANSFER_TIME*1000))
	# print("传输开始时间：%.2f ms" %(STARTTRANSFER_TIME*1000))
	# print("传输总结束时间：%.2f ms" %(TOTAL_TIME*1000))
	# print("下载数据包大小：%d bytes/s" %(SIZE_DOWNLOAD))
	# print("HTTP头部大小：%d byte" %(HEADER_SIZE))
	# print("平均下载速度：%d bytes/s" %(SPEED_DOWNLOAD))
	jsonObj = json.loads(t.contents)
	
	formatJsonStr = json.dumps(jsonObj,indent=4,ensure_ascii=False,sort_keys=True)
	#print formatJsonStr

	return jsonObj

	
	#print type(jsonObj['data']['volumes'])


	
if __name__ == '__main__':

	#l = [2784797,2746787,2476542,2856400,2825380,2839610,2402840,2747882,2689319,2734946,2816318,2425176,1797752,2820143,1430462,2847361,2474610,2435790,2738528,2797976,2797016,1868184,2575507,2213315,2402840,2485830,2754498,2398516,2754900,2720470,2783259,2686894,916533,2402178,2185865,2793325,2731646,2759944,2746837,2689319,2786516,2789348,2764221,2823104,2843305,2793325,2816318,2809509,2402178,2686894,2805000,2839738,2387745,2847361,2754498,2735469,2772164,2752330,2832418,2782672,2764925,2847394,2819519,2809119,2813768,2856885,2803700,2797708,2832097,2836190,2839060,1949748,2743240,2851227,2686965,2781997]
	#l = [2784797,2746787,2476542,2856400,2839610,2402840,2747882,2689319,2734946,2816318,2425176,1797752,2820143,1430462,2847361,2474610,2435790,2738528,2797976,2797016,1868184,2575507,2213315,2402840,2485830,2754498,2398516,2754900,2720470,2783259,2686894,916533,2402178,2185865,2793325,2731646,2759944,2746837,2689319,2786516,2789348,2764221,2823104,2843305,2793325,2816318,2809509,2402178,2686894,2805000,2839738,2387745,2847361,2754498,2735469,2772164,2752330,2832418,2782672,2764925,2847394,2819519,2809119,2813768,2856885,2803700,2797708,2832097,2836190,1949748,2743240,2851227,2686965,2781997]
	l = [2435790,2855413,2308148,2871746,2453471,2783259,2337193,2790587,1975688,2694854,2720968,2698979,1845278,2714641,2868323,2804445,2735326,2805360,2835713,2702031,2816318,2696950,2735866,2850223,2858943,2825270,2625740,2763105,1224594,2848632,2476542,333521,2753686,2689672,2697238,2696741,2797575,2808712,2843305,2790179,2831804,2791019,2802420,2758789,2865068]
	#l = [2789353,2815617]
	for j in l:
		url = 'http://api.k.com/v2/book/'+str(j)+'/volumes?app_key='
		print(j)
		jsonObj = curlurl(url)
		result = [(item.get('code','NA'),item.get('id','NA'),item.get('chapters','NA')) for item in jsonObj['data']['volumes']]
		fp = open('/Users/sunflower/DownLoads/'+str(j)+'.txt','w+')
		s = 1;
		index = 0
		if result[0][0] == 100:
			index = 1
		for i in result[index][2]:
			if s > 20:
				break;
			s = s + 1
			id1 = i['id']
			name1 = i['name']
			jsonObj2 = curlurl('http://api.k.com/v2/book/'+str(j)+'/chapter/'+str(id1)+'/content?app_key=')
			content1 = jsonObj2['data']['content']
			fp.write(name1+"\n")
			fp.write(content1+"\n")
		fp.close()
