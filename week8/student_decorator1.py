class Student:
  def __init__(self, name, region):
    self.name = name
    self.region = region

  def __str__(self):
    return f"{self.name} is from {self.region}"

  @classmethod
  def get(cls):
    name = input("Name, please: ")
    region = input("Region, please: ")
    return cls(name, region)
  
def main():
  student = Student.get()
  print(student)

if __name__ == "__main__":
  main()
 