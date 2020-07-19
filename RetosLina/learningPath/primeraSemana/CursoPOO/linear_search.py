import random

def linear_search(list1, target):
  match = False

  for element in list1:  # O(n)
    if element == target:
      match = True
      break  # no me cambia el O

  return match

if __name__ == '__main__':
  list_size = int(input('Which size for the list? '))
  target = int(input('Wich number are you looking for? '))

  list1 = [random.randint(0, 100) for i in range(list_size)]

  found = linear_search(list1,target)
  print(list1)
  print(f'The number {target} {"is" if found else "is not"} in the list')
