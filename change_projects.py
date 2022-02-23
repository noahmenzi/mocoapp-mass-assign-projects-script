#!/usr/bin/python3

# importing the module
import json
import requests

# adjust to your moco domain
URL = "https://{{domain}}.mocoapp.com/api/v1/projects/"
 
 # Headers, replace YOUR_API_KEY
HEADERS = {
    "Content-Type": "application/json;",
    "Authorization": "Bearer YOUR_API_KEY"
}


print("This Python script helps you to change the project leader of a lot of Moco projects at once.")
old_id = input("Please enter the id of the project leader which should be replaced by a new one: ")
print("Great. This is the list of projects assigned to this project leader:")

querystring = {"leader_id":old_id, "include_archived":"false"}
projects = requests.request("GET", URL, headers=HEADERS, params=querystring)
data = projects.json()

print("The following projects will be changed:")
for i in data:
    print(i['id'], i['name'])

new_id = input("Please enter the id of the new project leader. This new leader will be assign to all projects of the old project leader: ")

for i in data:
    project_url = URL + str(i['id'])
    print(project_url)
    response = requests.request("PUT", project_url, data={'leader_id' : new_id}, headers=HEADERS)
    print(response.status_code)

print("Success!")
