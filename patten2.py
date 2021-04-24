n = int(input())
k=1
c=1
n=n+1
for i in range(1,n):
    print(" "*(n-i-1)+"*"*i,end=" ")
    for j in range(1,i+1):
        print(str(k),end="")
        k=k+1
    print(end="\n")
for i in range(n,1,-1):
    k=n-1
    print(" "*(n-i),end="")
    for j in range(1,i):
        print(str(k),end="")
        k=k-1
    print(end=" ")
    c=2*(n-i)+1
    for j in range(1,i):
        print(str(c),end="")
        c=c+2
    print(end="\n")
