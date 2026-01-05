import random

def main():

  n = get_int()

  guess(n)


def get_int():
  while True:
    try:
      n = int(input("Level: "))
      if n < 1:
        continue
      return n
    
    except ValueError:
      continue

def guess(n):
  random_number = random.randint(1, n)

  while True:
    try:
      your_guess = int(input("Guess: "))
      if your_guess < 1:
        continue

      if your_guess < random_number:
        print("Too small! ")
        continue
      elif your_guess > random_number:
        print("Too big! ")
        continue
      else:
        print("Just right! ")
        break

    except ValueError:
      continue

main()