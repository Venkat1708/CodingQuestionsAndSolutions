"""
print string next position without change in space

ex: 
hello welcome

o/p:
iffmp xfmdpnf
"""


s=input()
s2=""
for i in s:
    if i!=" ":
        s2+=chr(ord(i)+1)
    else:
        s2+=i
print(s2)