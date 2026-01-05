name = input("Whats your name? ")

""" file = open("names.txt", "a")
file.write(f"{name}\n")
file.close() """

# If i use with, i dont need to close the file
with open("names.txt", "a") as file:
  file.write(f"{name}\n")