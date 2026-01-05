""" with open("names.txt", "r") as file:
  # lines = file.readlines()
  for line in file:
    # rstrip() for removing extraneous line break at the end of each line.
    print("hello", line.rstrip()) """


names = []

with open("names.txt", "r") as file:
  for line in file:
    names.append(line.rstrip())

  for name in sorted(names):
    print("hello,", name)