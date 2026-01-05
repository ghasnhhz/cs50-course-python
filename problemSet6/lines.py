import sys
import os

def main():

  if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
  elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
  elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")
  elif not os.path.isfile(sys.argv[1]):
    sys.exit("File does not exist")

  file = sys.argv[1]
  number_of_lines = get_num_of_lines(file)
  print(f"Number of non-empty lines in {file}: {number_of_lines}")


def get_num_of_lines(file_name):
  count = 0

  try:
    with open(file_name, "r") as file:
      for line in file:
        if line.strip() == "" or line.strip().startswith("#"):
          continue
        else:
          count += 1


  except FileNotFoundError:
    print("File Not Found")
    return
    
  return count


if __name__ == "__main__":
  main()
