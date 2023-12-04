import datetime
class Person:
  def __init__(self):
    self.BIRTHDATE = int(input("What is your birthdate? "))
    self.NAME = str(input("What is your name? "))
    self.COUNTRY = str(input("What country are you from? "))
    self.CURRENT = int(datetime.date.today().strftime("%Y"))
    self.AGE = 0

  def calculateAge(self):
    self.AGE = self.CURRENT - self.BIRTHDATE

  def getAge(self):
    return self.AGE


PERSON = Person()
PERSON.calculateAge()
print(PERSON.getAge())
