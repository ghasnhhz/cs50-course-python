""" students = []

with open("students.csv") as file:
  for line in file:
    name, house = line.strip().split(",")
    students.append(f"{name} is in {house}")

  for student in sorted(students):
    print(student) """


""" students = []

with open("students.csv") as file:
  for line in file:
    name, house = line.strip().split(",")
    student = {"name": name, "house": house}
    students.append(student)
  
  for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student["name"]} is in {student["house"]}") """


""" import csv

students = []

with open("students.csv") as file:
  reader = csv.reader(file)
  for row in reader:
    # The above row itself is a list: print(row)
    students.append({"name": row[0], "house": row[1]})
  
  for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student["name"]} is in {student["house"]}") """


import csv

students = []

with open("students.csv") as file:
  reader = csv.DictReader(file)
  for row in reader:
    # The row above is a dict: print(row)
    students.append(row)

  for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student["name"]} is in {student["home"]}")