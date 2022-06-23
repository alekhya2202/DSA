n, k, p = list(map(int, input().strip().split()))

arr = list(map(int, input().strip().split()))

arr = [[arr[i], (i+1)] for i in range(n)]
#print("arr =", arr)

arr = sorted(arr, key = lambda x: x[0])
#print("arr =", arr)
d=dict()

for i in range(n):
    d[arr[i][1]] = i

#print("d = ", d)

b = [0]*(n) 
for i in range(1,n):
    if(arr[i][0]-arr[i-1][0]<=k):
        b[i]=b[i-1]+1
#print(b)


for _ in range(p):
    x, y = list(map(int, input().strip().split()))
    x = d[x]; y = d[y]

    if(y<x):
        x,y = y,x

    if(x>=y-b[y]):
        print("Yes")
    else:
        print("No")
