k=int(input())
n=int(input())
numbers=list(map(int,input().split()))
b={}

if n%k==0:
    x=n//k
    for i in numbers:
        if i in b:
            b[i]+=1
            if b[i]>x:
                print('NO')
                break
        else:
            b[i]=1
    print('Yes')
else:
    print('NO')
