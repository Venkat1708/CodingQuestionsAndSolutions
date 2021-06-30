'''
To count noof time x-digit  occured in  the range of (l,u) inclusive
eg:
l=2
u=25
x=2
output:
9
Explaination:
2,12,20,21,22,23,24,25 are following numbers contains the digit 2,
So the count is 9 because in 22 there are 2 two's so 2 is counted twice in this case ie
count=1+1+1+1+2+1+1+1=9
'''
def countDigitOcurrences(l,u,x):
    count=0
    for i in range(l,u+1):
        n=i
        while(n!=0):
            rem=n%10
            if rem==x:
                count+=1
            n//=10
    return count
l=int(input())
u=int(input())
x=int(input())
c_o=countDigitOcurrences(l,u,x)
print(c_o) 