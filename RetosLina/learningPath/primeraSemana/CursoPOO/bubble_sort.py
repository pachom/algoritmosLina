import random

def bubble_sort(list1):

  n = len(list1)

  for i in range(n):
    for j in range(0, n - i - 1):

      if list1[j] > list1[j + 1]:
        list1[j], list1[j + 1] = list1[j + 1], list1[j]

  return list1


if __name__ == '__main__':
  list_size = int(input('Which size for the list? '))
  target = int(input('Wich number are you looking for? '))

  list1 = [random.randint(0, 100) for i in range(list_size)]
  print(list1)

  ordered_list = bubble_sort(list1)
  print(ordered_list)
