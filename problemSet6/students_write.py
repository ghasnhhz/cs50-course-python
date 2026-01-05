import csv
import os

#This checks whether the file students.csv already exists.
#Returns True if it exists, False otherwise.
file_exists = os.path.isfile("students.csv")

#If the file exists, it will run the left part → os.path.getsize(...) == 0 → and 
# return True or False depending on whether the file is empty or not(==0 or not).
#If the file does not exist, it just skips the check and directly 
# returns True — assuming the file will be empty once created.
is_empty = os.path.getsize("students.csv") == 0 if file_exists else True

name = input("Whats name? ")
home = input("Whats home? ")

with open("students.csv", "a", newline="") as file:
  writer = csv.DictWriter(file, fieldnames=["name", "home"])

  if is_empty:
    writer.writeheader()  # Write the header only if the file is empty

  writer.writerow({"name": name, "home": home})

students = []

with open("students.csv") as file:
  reader = csv.DictReader(file)
  for row in reader:
    students.append(row)

  for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student["name"]} is in {student["home"]}")