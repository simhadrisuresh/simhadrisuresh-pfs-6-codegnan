#chefteam
'''
t = int(input())
for i in range (t):
    n = int(input())
    ev = []
    ov = []
    for i in range (1,n+1):
        if n%i==0 and i%2==0:
            ev.append(i)
        elif n%i==0 and i%2!=0:
            ov.append(i)
    if len(ev)==len(ov):
        print(1)
    else:
        print(0)
'''
#shorted array
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))[:n]
    res = []
    for i in arr:
        if i  not in res:
            res.append(i)    
    print(*res,sep=" ")

            
#test3
t = int(input())
for i in range(t):
    n,x=map(int,input().split())
    a = list(map(int,input().split()))[:n]
    c = list(map(int,input().split()))[:n]
    fc = 0
    for _ in range(n):
        if a[i]>=x:
             fc = fc = c[i]
    print(fc)         


