import requests

for i in range(1970,2013):
    requests.delete('http://10.100.10.129:9200/apilog-'+str(i)+'.*')
    print(i)

for i in range(2018,2039):
    requests.delete('http://10.100.10.129:9200/apilog-'+str(i)+'.*')
    print(i)

print('ok')