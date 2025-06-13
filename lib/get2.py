import requests

url = "https://learn-co-curriculum.github.io/json-site-example/"

respone = requests.get(url)

print(respone.text)
