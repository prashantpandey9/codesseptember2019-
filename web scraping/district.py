"""This script is used to track the total case in india."""
import requests
import time
import json
url="https://api.covid19india.org/state_district_wise.json"
q=(requests.get(url)).text
data=json.loads(q)
print(data)
for j in data:
    for a in j:
        print(a["districtData"])
    break
