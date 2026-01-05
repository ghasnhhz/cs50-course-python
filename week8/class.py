class Student:
  def __init__(self, name, region):
    if not name:
      raise ValueError("Missing name! ")
    elif region not in ["Toshkent", "Samarqand", "Khorazm", "Bukharo"]:
      raise ValueError("Invalid region")
    self.name = name
    self.region = region

  def __str__(self):
    return f"{self.name} is from {self.region}"
    

def main():
  student = get_name()
  print(student)


def get_name():
  name = input("Name, please: ")
  region = input("Home, please: ")

  return Student(name, region)

if __name__ == "__main__":
  main()