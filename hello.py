""" name = input("What is your name? ")
print("hello \"friend\"")

# Remove whitespaces from the name input
name = name.strip()

# Capitalize the first letter of each word
name = name.title()

print(f"hello, {name}") """

def main():
  name = input("Whats your name? ")
  print(hello(name))

def hello(name="world"):
  return f"hello, {name}"


if __name__ == "__main__":
  main()