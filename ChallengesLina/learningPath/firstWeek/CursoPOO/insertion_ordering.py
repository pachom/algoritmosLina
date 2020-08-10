import random

def insertion_ordering(list1):

  
  for i in range(1,len(list1)):
    actual_value = list1[i]
    j = i
    while j > 0 and list1[j-1] > actual_value:
        list1[j] = list1[j - 1]
        j -= 1

    list1[j] = actual_value

  return list1


if __name__ == '__main__':
  list_size = int(input('Which size for the list? '))
  
  list1 = [random.randint(0, 100) for i in range(list_size)]
  print(list1)

  ordered_list = insertion_ordering(list1)
  print(ordered_list)