#https://www.youtube.com/watch?v=q6RicK1FCUs

tc = int(input())

def TOH(n : int, A, B, C):
    if n == 0:
        return
    
    TOH(n - 1, A, C, B)
    print("Move", n, "from", A , "to", C)
    TOH(n - 1,B , A, C)

    
for _ in range(tc):
    n = int(input())
    print(2 ** n - 1)
    TOH(n, 'A', 'B', 'C')
