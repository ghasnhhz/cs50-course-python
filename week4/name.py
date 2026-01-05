import sys

try:
  print("hello, my name is", sys.argv[1])
except:
  print("Too few arguments")