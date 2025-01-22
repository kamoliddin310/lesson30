import json


f = open('users.json')

json_data = f.read()

users_list = json.loads(json_data)


print(min(users_list, key=lambda user: user['age']))
