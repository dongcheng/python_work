import redis

r = redis.Redis(host='172.30.74.194',port=6379,db=1)
r.lpush("test_log", '''{"MCC":"","MNC":"","channel_id":"363","channel_title":"热度","ctime":"1431941690431","event_name":"NEWS","isoCC":"","latitude":"","longitude":"","network_state":"wifi","news_id":"yh","news_title":"yh","source":"DEFAULT","sp":"","user_id":"","user_name":"","user_type":"","visit_id":"9f9675be-3260-4aaa-9d41-d246724b9124","visit_start_time":"1431941337802","baseObjId":29,"ip":"58.68.145.131","app_key":"10_2015_04_06","udid":"357748059403926","channel_num":"无","client_ver":"4.2.3","client_code":"53","platform":"android","device_os":"4.4.2","device_model":"GT-I9508","device_product":"samsung","device_size":"1080.0x1920.0"}''')
print('ok')