text = input("Input: ")

newText = ""

# A set
vowels = {"A", "a", "E", "e", "I", "i", "O", "o", "U", "u"}

for i in text:
  if i in vowels:
    continue
  else:
    newText += i

print("Output: ", newText)