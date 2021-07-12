"""
To print series 1 2 5 8 15 so on ie tribonnaci for upto n number

Example:
i/p
2 -indicates test cases
4
1
o/p:
1 2 5 8
1


"""
t=int(input())
for i in range(t):
    n=int(input())
    a=[1,2,5]
    for i in range(3,n):
        a.append(a[i-1]+a[i-2]+a[i-3])
    if n<4:
        print(*a[:n])
    else:
        print(*a)
