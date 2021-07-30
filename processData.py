"""

example:
n=2
m=3
A1=[1,2]
A2=[-4,-5,-7]
o/p:
[1,-4,2,-5,-7]
Explanation:
1st element from A1 and 1st element from A2 and so..on

"""
def processData(n,m,A1,A2):
    l=[]
    for i in range(n+m):
        if i%2==0:
            if len(A1)!=0:
                s=A1.pop(0)
                l.append(s)
            else:
                s=A2.pop(0)
                l.append(s)
        else:
            if len(A2)!=0:
                s=A2.pop(0)
                l.append(s)
            else:
                s=A1.pop(0)
                l.append(s)
    print(l)

n=int(input())
m=int(input())
A1=list(map(int,input().split(" ")))
A2=list(map(int,input().split(" ")))
processData(n,m,A1,A2)