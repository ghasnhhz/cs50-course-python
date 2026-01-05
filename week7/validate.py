email = input("What's your email? ").strip()

username, domain = email.split("@")
print(f"Username: {username}, Domain: {domain}")

if username and domain.endswith(".com"):
  print("Valid")
else:
  print("Invalid")