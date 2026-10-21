import requests
import urllib.request
import json

api_key = ""
with open(".env") as f:
    for line in f:
        if line.startswith("NASA_API_KEY="):
            api_key = line.strip().split("=")[1]
            break
url = f"https://science.nasa.gov/wp-json/wp/v2/apod-basic/?api_key={api_key}"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    with open("apod.json", "w") as f:
        json.dump(data, f, indent=4)
else:
    print(f"Error: {response.status_code}")

    image_8sas
