def main():

  text = input("Write a word followed by :) or :( ")
  print(convert(text))


def convert(text):
  text = text.replace(":)", "🙂")
  text = text.replace(":(", "🙁")

  return text

main()