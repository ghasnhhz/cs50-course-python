import re

url = input("URL: ").strip()

username = re.sub("^(htpps?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")