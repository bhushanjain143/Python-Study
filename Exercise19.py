'''
from time import time

def timer(func):
    def wrapper(n):
        t1 = time()
        result = func(n)
        t2 = time()
        print(t2 - t1)
        return result
    return wrapper

@timer
def sum_1m(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return(sum)

x =  sum_1m(100)
print(x)
'''
'''
l = [99,1,2,3,4,5]
x = list(map(lambda i:i**3,l))
print(x)


lst = [10,11,12,13,14]
op = filter(lambda i: i % 2 == 0, lst) 
print(op)
 
 
from  functools import reduce

l = [99,1,2,3,4,5]
product  = lambda a,b :a * b
print(reduce(product,l))

pro  = list(reduce(lambda a,b :a * b,l))
print("PRO",pro)



lst = [99,1,2,3,4,5]

ano = [i for i in lst if i % 2 == 0] 
print(ano)

'''
'''
lst = [99,1,2,3,4,5]

def sum_all(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

xx = sum_all(99,1,2,3,4,5)
print(xx)

'''


for i in range(-1,5):
    print(i * "*")