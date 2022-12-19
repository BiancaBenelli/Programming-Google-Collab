def succ(n):
    print(n+1)

succ(3)

def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

if __name__ == '__mai__':
    for i in range(20):
        print(is_prime(i))