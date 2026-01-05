fruits = {

}

while True:
  try:
    fruit = input(" ").strip().lower()
    if fruit in fruits:
      fruits[fruit] += 1
    else: 
      fruits[fruit] = 1

  except EOFError:
    break

for key in sorted(fruits):
  print(f"{fruits[key]} {key.upper()}")