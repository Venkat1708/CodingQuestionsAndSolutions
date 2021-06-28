"""
Print sum of the max subsets and the subset in an array
eg:a=[-2, -3, 4, -1, -2, 1, 5, -3]
sum of max subset is 7
and subset is [4, -1, -2, 1, 5]

"""

#sum  of max of subset in an array
a=list(map(int,input().split(",")))
l=[]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        l.append(a[i:j])

s=[]
for i in l:
    v=sum(i)
    s.append(v)
print(max(s)) 
# to print the sum max subset in array
for i in l:
    if sum(i)==max(s):
        print(i)
   