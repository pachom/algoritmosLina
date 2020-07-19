class Person:

  def __init__(self,name):
    self.name = name

  def get_moving(self):
    print('keep walking')

class Cyclist(Person):

  def __init__(self,name):
    super().__init__(name)

  def get_moving(self):
    print('keep riding a bike')

def main():
  person = Person('David')
  person.get_moving()

  cyclist = Cyclist('Daniel')
  cyclist.get_moving()

if __name__ == '__main__':
  main()
