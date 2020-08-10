class Voting_box:
  
  def __init__(self, identifier, country):
    self._identifier = identifier
    self._country = country
    self._region = None

  @property
  def region(self):
    return self._region

  @region.setter
  def set_region(self, region):
    if region in self._country:
      self._region = region
    else:
      raise ValueError(f'La region {region} no es valida en {self._country}')

if __name__ == '__main__':  
  box = Voting_box(123, ['Bogota', 'Cali'])
  print(box.region)  
  box._region = 'Cali'  
  print(box.region)  