import json
import requests

base_url = 'https://petstore.swagger.io/v2'

# 1 POST запрос - /user - Create user
headers1 = {'accept': 'application/json',
           'Content-Type': 'application/json'}
data1 = {
  "id": 0,
  "username": "SobachkinF",
  "firstName": "Sobachkin",
  "lastName": "Friend",
  "email": "Sobachkin@mail.ru",
  "password": "54321",
  "phone": "+74952223344",
  "userStatus": 0
}
data1=json.dumps(data1)
res1 = requests.post(f'{base_url}/user', headers= headers1, data= data1)
print(res1.status_code)
print(res1.json())


# 2 GET запрос - /store/inventory - Returns pet inventories by status
#base_url = 'https://petstore.swagger.io/v2'
headers2 = {'accept': 'application/json'}
res2 = requests.get(f'{base_url}/store/inventory', headers=headers2)
print(res2.status_code)
print(res2.json())

# 3 PUT запрос - /pet - Update an existing pet
#base_url = 'https://petstore.swagger.io/v2'
headers3 = {'accept': 'application/json',
            'Content-Type': 'application/json'}
data3 = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
data3 = json.dumps(data3)
res3 = requests.put(f'{base_url}/pet', headers=headers3, data=data3)
print(res3.status_code)
print(res3.json())


# 4 PUT запрос - /user/{username}-  Updated user
username = 'Doggy'
#base_url = 'https://petstore.swagger.io/v2'
headers4 = {'accept': 'application/json', 'Content-Type': 'application/json'}
data4 = {
  "id": 0,
  "username": "string",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "userStatus": 0
}
res4 = requests.put(f'{base_url}/user/{username}', headers=headers4, data=data4)
print(res4.status_code)
print(res4.json())


# DELETE запрос - /store/order/{orderId} - Delete purchase order by ID
orderId = 5
#base_url = 'https://petstore.swagger.io/v2'
headers5 = {'accept': 'application/json'}
res5 = requests.delete(f'{base_url}/store/order/{orderId}', headers=headers5)
print(res5.status_code)
print(res5.json())