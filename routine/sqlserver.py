from os import getenv
import pymssql
import requests
import urllib
import array
import re

conn = pymssql.connect('10.100.6.123', 'sa', 'jinzhao#EDC', 'paperSpiderBak')
cursor = conn.cursor()
cursor.execute("SELECT * FROM TempUrlNewsPapers201604 where pubtime >= '2016-03-25 00:00:00.000' and pubtime < '2016-04-01 00:00:00.000' ")

count = 0

for row in cursor:
    ##print('row = %r' % (row,))
    #print(row[10])
    if(None == row[0]):
        break

    if(None == row[10]):
        continue

    print(str(row[0])+ ' : '  + str(count))

    html=str(row[10])
    dr = re.compile(r'<[^>]+>',re.S)
    dd = dr.sub('',html)

    if (dd.strip()!=''):
        body = dict(ifLabel=0, id='docExtrator', content=dd)
        print('start request ...........')
        r = None
        try:
            r = requests.post('http://10.100.10.124:8080/PeopleWebClient/index/getAllContent.do',body,timeout = 1)
        except requests.exceptions.Timeout as e:
            print("time out error")
        print('end request ...........')
        #print(r.text)
        if(r is not None and r.text.strip() != ''):
        	data = eval(r.text)


        	if('江西' in data[1] or '江西' in data[7]):
        		out = "<REC>" + "\t\n"
        		out = out + "<地名>=" + data[1] + "\t\n"
        		out = out + "<关键词>=" + data[3] + "\t\n"
        		out = out + "<省名>=" + data[7] + "\t\n"
        		out = out + "<摘要>=" + data[8] + "\t\n"
        		out = out + "<情感>=" + data[9] + "\t\n"
        		out = out + "<ID>=" + str(row[1]) + "\t\n"
        		out = out + "<标题>=" + str(row[6]) + "\t\n"
        		out = out + "<副标题>=" + str(row[55]) + "\t\n"
        		out = out + "<肩标题>=" + str(row[67]) + "\t\n"
        		out = out + "<报名>=" + str(row[59]) + "\t\n"
        		out = out + "<版次>=" + str(row[69]) + "\t\n"
        		out = out + "<版名>=" + str(row[70]) + "\t\n"
        		out = out + "<作者>=" + str(row[49]) + "\t\n"
        		out = out + "<正文>=" + str(row[10]) + "\t\n"
        		out = out + "<日期>=" + str(row[18]) + "\t\n"
        		out = out + "<链接>=" + str(row[45]) + "\t\n"

        		try:
        			with open('/home/cheng/paper201604.txt', 'a') as f:
        				f.write(out)
        				f.write("\t")
        				f.write('\n')
        		except ValueError as e:
        			print("error")

        		count=count+1
        		print(count)

print('end')

conn.close()