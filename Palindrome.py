n=int(input())
t=n
rev=0
while n>0:
    s=n%10
    rev=rev*10+s
    n=n//10
if t==rev:
    print("True")
else:
    print("False")