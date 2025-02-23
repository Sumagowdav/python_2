# this below program fetch the user and login name who made pull request on kubernetes open repository
# whenever you use response.json() it converst the json format data into dictnories

import requests
response =requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
#print(response.json())
complete_details = response.json()

for i in range(len(complete_details)):
    print(complete_details[i]["user"]["login"])