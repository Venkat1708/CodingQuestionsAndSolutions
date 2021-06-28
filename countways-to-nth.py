"""
count noof ways to reach nth stair by taking atmost m steps jump.

"""
def Possibleways(n,m):
    if n==0:
        return -1
    else:
        return countWays(n+1,m)
def countWays(n,m):
    if n<=1:
        return n
    else:
        res=0
        i=1
        while(i<=n and i<=m):
            res+=countWays(n-i,m)
            i+=1
    return res
n=int(input())
m=int(input())
steps=Possibleways(n,m)
print("No of ways to reach {}th step by taking atmost {} steps at a time is {}".format(n,m,steps))