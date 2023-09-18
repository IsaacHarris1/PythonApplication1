import requests

data = {
    "key1": "value1",
    "key2": "value2",
    "key3": "your mom"
}

url = "http://localhost:5000/store_data"

response = requests.post(url,json=data)

if response.status_code == 201:
    print("data stored successfully")
else:
    print("failed to store data",response.status_code)
    
url = "http://localhost:5000/get_data"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("stored data:",data)
else:
    print("failed to retrieve data. Status code", response.status_code)    
    
url = "http://localhost:5000/purge_data"
response = requests.delete(url)

if response.status_code == 200:
    data = response.json()
    print("DataPurged:",data)
else:
    print("failed to purge data. Status code", response.status_code)    