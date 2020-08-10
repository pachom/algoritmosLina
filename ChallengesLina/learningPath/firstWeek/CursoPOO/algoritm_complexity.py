import time
import sys



def factorial(n):
  answer = 1

  while n > 1:
    answer *= n
    n -= 1

  return answer

def factorial_r(n):
  if n == 1:
    return 1
  else:
    return n * factorial_r(n-1)


if __name__ == '__main__':
  
  n = 5000

  begin = time.time()
  factorial(n)
  end = time.time()
  print(end - begin)

  begin = time.time()
  factorial_r(n)
  end = time.time()
  print(end - begin)