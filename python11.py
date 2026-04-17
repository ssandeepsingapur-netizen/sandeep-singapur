import requests

URL = input("Enter website URl: ")
response = requests.get(URL)

if response.status_code == 200:
    print("Website is up")
else:
    print("Website is down")