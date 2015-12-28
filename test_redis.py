import redis
r = redis.Redis(host='172.30.74.194',port=6379,db=1)
r.set('foo','ba2r00000aa')
print('a')