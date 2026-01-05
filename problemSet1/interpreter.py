expression = input("Enter an integer and an arithmetic expression(* / + - ) and an integer: ")
x, y, z = expression.split(" ")
x = float(x)
z = float(z)

result = 0

if y == "+":
  result = x + z
elif y == "-":
  result = x - z
elif y == "*":
  result = x * z
elif y == "/":
  result = x / z

print(f"{result:.1f}")