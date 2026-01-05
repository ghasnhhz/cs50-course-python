def main():

  text = input("Say something: ").lower()

  result = greeting(text)
  print(result)

def greeting(text):
  if text.startswith("hello"):
    return "$0"
  elif text.startswith("h"):
    return "$20"
  else:
    return "$100"

if __name__ == "__main__":
  main()