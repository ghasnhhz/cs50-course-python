class Wizard:
  def __init__(self, name):
    self.name = name


class Student(Wizard):
  def __init__(self, name, house):
    super().__init__(name)
    self.house = house



wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
print(student.name, student.house)