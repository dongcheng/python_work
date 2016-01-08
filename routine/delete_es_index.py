import requests

#error data not betweent 2013 ~ 2017

years =  list(range(1970,2013)) +  list(range(2018,2039))

for year in years:
    requests.delete('http://10.100.10.129:9200/apilog-'+str(year)+'.*')
    print(year)

print('ok')