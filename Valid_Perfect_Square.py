import math
t=int(input())
for i in range(1,t+1):
    n=int(input())
    m=int(math.sqrt(n))
    if n==m*m:
        print('True')
    else:
        print('False')