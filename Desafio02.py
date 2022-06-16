import math


def fibo(n):
    if n == 0:
      return 0
    elif n ==1:
      return 1
    else:
        return fibo(n - 2) + fibo(n - 1)

n = int(input('QUANTOS TERMOS VOCÊ QUER MOSTAR? : '))

for x in range(n):
    print(fibo(x), end=' ')



def quadrado_perfeito(n):
    s = int(math.sqrt(n))
    return s * s == n

def Validando_fibonacci(n):
    return quadrado_perfeito(5*n*n + 4) or quadrado_perfeito(5*n*n - 4)


if(Validando_fibonacci(n) == True):
    print(f"\n{n} Faz parte da sequência de Fibonacci")
else:
    print(f"\n{n} não faz parte da sequência de Fibonacci")