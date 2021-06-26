"""
Given a string s in lowercase and character X

Given an integer Y

Find the total number of substrings having exactly Y times character X.

Input: The first argument given is the String S. The second argument given is character X.

The third argument given is Integer Y

Output: print total number of substrings having exactly Y times character X.

Constraints 1 <= len(S) <= 100000

X in lowercase

1<=T<=100000

Sample Input: S =ravan

X=a

Y = 2

Sample Output 4

"""

s=input().lower()
X=input()
Y=int(input())
l=[]
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        l.append(s[i:j])
s=set(l)
l2=list(s)
c=0
for i in l2:
    if i.count(X)==Y:
        c+=1

print(l2)#substrings
print(c)#count