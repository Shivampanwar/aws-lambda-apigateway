import requests

url = 'http://localhost:8080/2015-03-31/functions/function/invocations'
# data = {'url': 'http://bit.ly/mlbookcamp-pants'}
data1 = {"values":[[0.1,2,0.1,3]]}
data2 ={"values":[[5.9,3.0,5.1,2.3]]}
result1,result2 = requests.post(url, json=data1).json(),requests.post(url, json=data2).json()
print(result1,result2)