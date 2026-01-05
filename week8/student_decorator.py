class Student:
  def __init__(self, name, region):
    self.name = name
    self.region = region

  def __str__(self):
    return f"{self.name} is from {self.region}"
  
  # getter for name
  @property
  def name(self):
    return self._name
  
  # setter for name
  # setters are called whenever the properties are set. For example, with student.house = "Gryffindor"
  @name.setter
  def name(self, name):
    if not name:
      raise ValueError("Missing name! ")
    self._name = name

  
  # getter for region
  @property
  def region(self):
    return self._region
  

  # setter for region
  @region.setter
  def region(self, region):
    if region not in ["Toshkent", "Samarqand", "Khorazm", "Bukharo"]:
      raise ValueError("Invalid region")
    self._region = region
    

def main():
  student = get_name()
  print(student)
  student.region = "Bukharo"
  print(student)


def get_name():
  name = input("Name, please: ")
  region = input("Home, please: ")

  return Student(name, region)

if __name__ == "__main__":
  main()