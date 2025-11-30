import math
fun = lambda x : 1 if x == 1 else math.ceil(math.sinh(fun (x-1)))
print('------------------')
print(fun(5))
print('------------------')