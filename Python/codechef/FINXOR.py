c=int(input())
for i in range(22):
    a=[0]*i
a[0]=1
for i in range(1,21):
    a[i]=2*a[i-1]
while(c!=0):
    n=int(input())
    print(1," ",a[20])
    sum1=int(input())
    sum1=sum1-(a[20]*n)
    xor=0
    if(sum1%2!=0):
        xor=xor+1
    for i in range(1,20):
        usersum=sum1+(a[i]*n)
        print(1," ",a[i])
        givensum=int(input())
        if(((usersum-givensum)/(a[i]*2))%2!=0):
            xor=xor+a[i]
    print(2," ",xor,"\n")
    output=int(input())
    c=c-1
