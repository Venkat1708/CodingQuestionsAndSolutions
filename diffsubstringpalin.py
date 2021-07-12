"""
Difference btw longest substring palin and smallest substring palin
Example:
abac
o/p:
2
Explanation:
longest substring plaindrome is aba whose length is 3
smallest substring plaindrome is a whose length is 1
==>Now their difference is 3-1=2

"""
s=input()
l=[]
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        l.append(s[i:j])
l2=[]
for i in l:
    if i==i[::-1]:
        l2.append(len(i))

print(max(l2)-min(l2))   