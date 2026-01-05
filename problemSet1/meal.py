def main():

  time = input("What time is it? ")

  hours, minutes = time.split(":")
  hours = float(hours)
  minutes = float(minutes)

  convertedTime = convert(hours, minutes)

  if 7 <= convertedTime <= 8:
    print("Breakfast time ")
  elif 12 <= convertedTime <= 13:
    print("Lunch time ")
  elif 18 <= convertedTime <= 19:
    print("Dinner time ")
  

def convert(hours, minutes):
  return hours + (minutes / 60)


main()