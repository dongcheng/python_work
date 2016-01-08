#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import redis
import json
from pprint import pprint
import time

keys = ["app_key", "channel_id", "channel_num", "channel_title", "client_code", 
	"client_ver", "ctime", "destation", "device_model", "device_os", 
	"device_product", "device_size", "endtime", "event_name", 
	"identifier", "ip",
	"isoCC", "isoCe", "latitude", "longitude", "MCC", "message", "MNC", 
	"network_state", "news_id", "news_title", "platform", "source", "sp", 
	"startup", "state", "tags", "type", "udid", "user_id", "user_name", 
	"user_type", "visit_id", "visit_start_time", "deal_date"]

r = redis.Redis(host='10.100.10.179',port=6379,db=0,password='0928.7NAhTH7UnCxyd9.2015')
print(r.llen('apilog:ad'))

i = 0
flag = True
while  flag:
	start =  i * 1000
	end = start + 999
	logs = r.lrange("apilog:ad",start,end)
	if (logs == None  or len(logs) == 0):
		flag = False
		break
	for x in logs:
		try:
			data = json.loads(x.decode('utf-8'))
			with open('/home/cheng/adlog7.txt', 'a') as f:
				for key in keys:
					if(key == 'ctime'):
						timearray = time.localtime(int(data.get(key))/1000)
						f.write(time.strftime("%Y-%m-%d %H:%M:%S", timearray))
					else:
						f.write(str(data.get(key)))
					f.write("\t")
				f.write('\n')
		except ValueError as e:
			print(x.decode('utf-8'))
			continue
		
	print(i * 1000)
	i=i+1

print('处理完成!')