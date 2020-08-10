import random

def binary_search(list1, start, end, target):

  print(f'buscando {target} entre {list1[start]} y {list1[end -1]}')
  if start > end:
    return False

  half =(start + end) // 2   # // integer division  return an integer

  if list1[half] == target:
    return True
  elif list1[half] < target:
    return binary_search(list1, half + 1, end, target)
  else:
    return binary_search(list1, start, half -1, target)


if __name__ == '__main__':
  list_size = int(input('Which size for the list? '))
  target = int(input('Wich number are you looking for? '))

  list1 = sorted([random.randint(0, 100) for i in range(list_size)])

  found = binary_search(list1, 0, len(list1), target)

  print(list1)
  print(f'The number {target} {"is" if found else "is not"} in the list')
