class Car:
  def __init_(self, model, brand, color):
    self.model = model
    self.brand = brand
    self.color = color
    self._estado = 'in rest'
    self._motor = Motor(cylinders=4)

  def acelerate(self, type='slowly'):
    if type == 'rapid':
      self._motor.inject_gasoline(10)
    else:
      self._motor.inject_gasoline(3)

    self._estado = 'in movement'

class Motor:
  def __init__(self, cylinders, type='gasoline'):
    self.cylinders = cylinders
    self.type = type
    self._temperature = 0

    def inject_gasoline(self, quantity):
      pass