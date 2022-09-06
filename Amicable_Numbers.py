n=int(input())
m=int(input())
sum=0
summ=0
for i in range(1,n):
    if n%i==0:
        sum+=i
for i in range(1,m):
    if m%i==0:
        summ+=i
if sum==m and summ==n:
    print('Amicable')
else:
    print("Not Amicable")
            