import requests


result = requests.get("http://localhost:3000/users", timeout=1)

data = result.json()

if (len(data) == 4):
    print("ooook")
else:
    print("tests failed")