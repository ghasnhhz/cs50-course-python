amountDue = 50

print("Amount due:", amountDue)

while amountDue > 0:
  insertedCoin = int(input("Insert coin: "))

  if insertedCoin in [5, 10, 25]:
    amountDue = amountDue - insertedCoin
    if amountDue > 0:
      print("Amount due:", amountDue)
  else:
    print("Amount due:", amountDue)

# abs(-a) -> a
print("Change owed: ", abs(amountDue))