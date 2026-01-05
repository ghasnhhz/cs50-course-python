import json
import requests
import sys

if len(sys.argv) != 2:
  sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

o = response.json()
# result is the dict, and 0["results"] is the list.
for result in o["results"]:
  print(result["trackName"])

list = [
  {
    "name": "Shahzod",
    "surName": "Karimov",
  }
]

# here, i is the dict while dict is the list.
for i in dict:
  print(i)