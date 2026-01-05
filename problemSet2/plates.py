def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    extracted_number = ""
    for char in s:
      if char.isdigit():
        extracted_number += char

    first_two_characters = s[0:2]
    length = len(s)
    last_charater = s[-1:]

    if not first_two_characters.isalpha():
       return False
    elif not 2 <= length <= 6:
       return False
    elif extracted_number[0] == "0":
       return False
    elif last_charater.isalpha():
       return False
    else:
       return True


main()