camelCase = input("Write a camelCased word: ")

# We are creating this new variable as 
# We can not directly edit camelCase.
snake_case = ""

for char in camelCase:
  if char.isupper():
    snake_case += "_" + char.lower()
  else: 
    snake_case += char
  
print(snake_case)