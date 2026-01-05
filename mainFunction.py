# Why do we need to put the main first?
  # We put main first as we call it last:
    # until the interpreter reaches main(), it sees all function definitions
    # otherwise, it would give an error since python executes code line by line: 
    # when the enterpreter encounters a function call, it must have already seen
    # the function definition how to know how to execute it.
def main():

  name = input("Whats your name? ")
  sayHello(name)

  sayHello()


def sayHello(name="world"):
  print(f"hello, {name}")

main()