a=int(input())
b=int(input())
for j in range(a,b+1):
    n=j
    fc=0
    for i in range(1,n+1):
        if n%i==0:
            fc+=1
    if fc==2:
        print(n)