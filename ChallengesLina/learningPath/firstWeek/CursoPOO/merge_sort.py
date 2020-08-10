import random

def merge_sort(list1):
  if len(list1) > 1:
    middle = len(list1) // 2
    left = list1[:middle]
    right = list1[middle:]
    print(left, '+' * 5, right)

    #recursive call whith each half
    merge_sort(left)
    merge_sort(right)

    #iterator for each list
    i = 0
    j = 0
    #iterator for main list
    k = 0

    while i < len(left) and j < len(right):
      if left[i] < right[j]:
        list1[k] = left[i]
        i += 1
      else:
        list1[k] = right[j]
        j += 1
      
      k += 1
    
    while i < len(left):
      list1[k] = left[i]
      i += 1
      k += 1

    while j < len(right):
      list1[k] = right[j]
      j += 1
      k += 1

    print(f'left {left}, right {right}')
    print(list1)
    print('-' * 20)

  return list1
  


if __name__ == '__main__':
  list_size = int(input('Which size for the list? '))
  
  list1 = [random.randint(0, 100) for i in range(list_size)]
  print(list1)
  print('-' * 20)

  ordered_list = merge_sort(list1)
  print(ordered_list)