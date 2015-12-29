import redis
import json
from pprint import pprint

r = redis.Redis(host='172.30.74.194',port=6379,db=1)

while 1:
	log = r.rpop('test_log')
	if(log):
		data = json.loads(log.decode())
		print(data['ctime'])
		pprint(data)
	else:
		break

print('处理完成!')