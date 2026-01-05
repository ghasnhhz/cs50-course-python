def main():
  result = get_fraction()

  if result <= 1:
    print("E")
  elif result >= 99:
    print("F")
  else:
    print(f"{result}%")

def get_fraction():
  while True:
    try:
      fraction = input("Fraction: ")
      x, y = fraction.split("/")
      x = int(x)
      y = int(y)
      if x > y or y == 0:
        # we can not use pass since it just does nothing and other lines go on running
        # but continue skips the rest of the code, and the next iteration will start
        continue
    except (ValueError, ZeroDivisionError):
      # Here we can use pass as if there is an error, no further code will be executed
      # the next iteration starts, but if the return were in try, we would not use pass
      # since first except runs and then return runs, meaning that even if there occured 
      # an error in except, return would run AS IT IS NOT IN THE ELSE BLOCK.
      pass
    else:
      return round(x / y * 100)
    
main()
