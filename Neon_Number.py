n=int(input())
sum=0
s=n**2
while s>0:
    d=s%10
    sum+=d
    s=s//10
if sum==n:
    print("Neon Number")
else:
    print("Not Neon Number")
    
    