def main():
  text = input("Text: ")

  result = shorten(text)
  print(result)

def shorten(text):
  vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']

  shortened_text = ''

  for i in text:
    if i in vowels:
      continue
    else:
      shortened_text += i
  
  return shortened_text

if __name__ == "__main__":
  main()