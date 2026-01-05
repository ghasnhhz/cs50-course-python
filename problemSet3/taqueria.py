orders = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

while True:
  try:
    # .strip() only removes spaces at the start or end: does not remove the spaces between words.
    item = input("Item: ").strip().title()
    if item in orders:
      total += orders[item]
      print(f"Total: ${total:.2f}")
      # else: continue is not required. Just for style/understanding better
    else:
      continue

  except EOFError:
    break
