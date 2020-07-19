

def backpack(backpack_size, weights, values, n):
  print('-' * 20)
  print(f'backpack_size: {backpack_size}, weight: {weights[n-1]}, values: {values[n-1]} n: {n}')
  if n == 0 or backpack_size == 0:
    return 0
  
  if weights[n - 1] > backpack_size:
    #print(n)    #f'weights {n-1} {weights[n-1]} more than backpack_size {backpack_size} ')
    return backpack(backpack_size, weights, values, n-1)

  
  better_choise =  max(values[n -1] + backpack(backpack_size - weights[n -1], weights, values, n -1),
              backpack(backpack_size, weights, values, n - 1))
  print(f'better choise: {better_choise}')
  return better_choise


if __name__ == '__main__':
  values = [60,100,120]
  weights = [10, 20, 30]
  backpack_size = 50
  n = len(values)

  outcome = backpack(backpack_size, weights, values, n)
  print(outcome)