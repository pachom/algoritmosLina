
class Coordinate:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def distance(self, otra_coordenada):
    x_diff = (self.x - otra_coordenada.x)**2
    y_diff = (self.y - otra_coordenada.y)**2

    return (x_diff + y_diff)**0.5

""" __name__ is the entry point. for run from terminal is: """
if __name__ == '__main__':
  coord_1 = Coordinate(3, 30)
  coord_2 = Coordinate(4, 8)

  #print(coord_1.distance(coord_2))
  print(isinstance(coord_2, Coordinate))