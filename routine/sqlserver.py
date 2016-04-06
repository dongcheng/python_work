from os import getenv
import pymssql
import requests
import urllib
import array
import re

ZHP_SERVER = 'http://10.100.10.124:8080/PeopleWebClient/index/getAllContent.do'
OUT_FILE = '/Users/cheng/Documents/paper201604.txt'
SELECT_SQL = "SELECT * FROM TempUrlNewsPapers201604 where pubtime >= '2016-03-25 00:00:00.000' and pubtime < '2016-04-01 00:00:00.000'"

#去除html标签
def removeHtml(text):
	dr = re.compile(r'<[^>]+>',re.S)
	return dr.sub('',text)

#张华平分析文本
def zhp(text):
	result = None
	requestBody = dict(ifLabel=0, id='docExtrator', content=text)
	try:
		result = requests.post(ZHP_SERVER, requestBody, timeout=1)
	except Exception as e:
		print('request zhp server error ...')
	return result

#拼装数据
def joinData(dbrow,reponseBody):
	out = "<REC>" + "\t\n"
	out = out + "<地名>=" + reponseBody[1] + "\t\n"
	out = out + "<关键词>=" + reponseBody[3] + "\t\n"
	out = out + "<省名>=" + reponseBody[7] + "\t\n"
	out = out + "<摘要>=" + reponseBody[8] + "\t\n"
	out = out + "<情感>=" + reponseBody[9] + "\t\n"
	out = out + "<ID>=" + str(dbrow[1]) + "\t\n"
	out = out + "<标题>=" + str(dbrow[6]) + "\t\n"
	out = out + "<副标题>=" + str(dbrow[55]) + "\t\n"
	out = out + "<肩标题>=" + str(dbrow[67]) + "\t\n"
	out = out + "<报名>=" + str(dbrow[59]) + "\t\n"
	out = out + "<版次>=" + str(dbrow[69]) + "\t\n"
	out = out + "<版名>=" + str(dbrow[70]) + "\t\n"
	out = out + "<作者>=" + str(dbrow[49]) + "\t\n"
	out = out + "<正文>=" + str(dbrow[10]) + "\t\n"
	out = out + "<日期>=" + str(dbrow[18]) + "\t\n"
	out = out + "<链接>=" + str(dbrow[45]) + "\t\n"

	return out

#写文件
def writeFile(text):
	try:
		with open(OUT_FILE, 'a') as f:
			f.write(text)
			f.write("\t\n")
	except ValueError as e:
		print("error")

#主程序
def run():
    conn = pymssql.connect('10.100.6.123', 'sa', 'jinzhao#EDC', 'paperSpiderBak')
    cursor = conn.cursor()
    cursor.execute(SELECT_SQL)

    count = 0

    for row in cursor:
	    if(None == row[10]):
		    continue

	    print(str(row[0])+ ' : '  + str(count))
	    dd = removeHtml(str(row[10]))
	    if (dd.strip()!=''):
	    	r = zhp(dd)
	    	if(r is not None and r.text.strip() != ''):
		    	data = eval(r.text)
		    	if('江西' in data[1] or '江西' in data[7]): 
			    	out = joinData(row, data)
	    			writeFile(out)
		    		count=count+1
    print('end')
    conn.close()

run()