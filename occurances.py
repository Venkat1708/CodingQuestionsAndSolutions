"""
Find the occurrance of each element in list and print the elements which occurred only once
Example:
i/p:
1 1 5 2 4 2 3
o/p:
 1 2
 2 2
 3 1
 4 1
 5 1
 3 4 5#occurd only once
"""

l=list(map(int,input().split(" ")))
d={}
for i in l:
    d[i]=l.count(i)
for k,v in d.items():
    print(k,v)
for k in d:
    if d[k]==1:
        print(k,end=" ")
