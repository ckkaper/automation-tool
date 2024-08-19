import subprocess
import requests
import time

print("Running docker compose up")

subprocess.call(["docker", "compose", "up", "-d"])
while True:
    try: 
        healthcheckResult = requests.get("http://localhost:3000/ping", timeout=1)
        if healthcheckResult.ok:
            print("Successfully recieved healthcheck result")
            break
    except:
        print("Pending for healthcheck result")
    
    time.sleep(3)


print("Running prisma database seed")

subprocess.call(["docker", "exec", "-it", "boilerplate-app-skeleton-svc-1", "node", "./dist/prisma/seed.js"])

print("Successfully ran prisma seed")

print("Running integration tests")

subprocess.call(["py", "integration-tests.py"])

print("Succssfully ran integration tests")