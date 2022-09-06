m=int(input())
count=0
i=1
while m>=i:
    if m%i==0:
        count+=1
    i+=1
if count==2:
    print('prime')
else:
    print('not a prime')