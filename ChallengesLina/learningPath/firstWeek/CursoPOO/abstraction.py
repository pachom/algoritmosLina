class Washing_machine:
  def __init__(self):
    pass
  
  def wash(self,temperature ='hot'):
    self._fill_water_tank(temperature)
    self._add_javon()
    self._wash()
    self._spin_dry()

  def _fill_water_tank(self, temperature):
    print(f'filling the tank with {temperature} water')

  def _add_javon(self):
    print('adding javon')

  def _wash(self):
    print('washing the clothes')

  def _spin_dry(self):
    print('spinning the clothes')

if __name__ == '__main__':
  washing_machine = Washing_machine()
  washing_machine.wash()