from tabulate import tabulate 
import csv
import sys
import os

def main():
  if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
  elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
  elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
  elif not os.path.isfile(sys.argv[1]):
    sys.exit("File does not exist")

  file = sys.argv[1]
  tabulate_csv(file)

def tabulate_csv(file):
  try:
    with open (file, 'r') as file:
      reader = csv.reader(file)
      data = list(reader)

      headers = data[0]
      table_data = data[1:]

      print(tabulate(table_data, headers=headers, tablefmt="grid"))
              
  except FileNotFoundError:
    return

if __name__ == "__main__":
  main()