'''
to count the k-digit number in an array
eg: a=[1,22,2,3,23,42]
k=2
o/p: 3
Explaination :
22,23,42 are 2-digit numbers so count=3
'''
def countDigitNumbers(a,k):
    sc=0
    for i in a:
        n=i
        c=0
        while(n!=0):
            n//=10
            c+=1
        if c==k:
            sc+=1
    return sc
a=list(map(int,input().split(",")))
k=int(input())
count=countDigitNumbers(a,k)
print(count)