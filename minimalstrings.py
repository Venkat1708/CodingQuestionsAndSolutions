"""
In this task you have to find the minimal remaining string The minimal remaining string is as follows: Take a given string and find the maximal prefix which when reversed is also a suffix. Remove this prefix and suffix. What you have left now is the minimal remaining string

Input Format

The input consists of only one line - the string to be processed

Constraints

1<=length of string<=100

Output Format

The output consists of only a single line - the minimal remaining string If the minimal remaining string is empty print "Minimal string is empty" (without quotes)

Sample Input 0

abcdjklcba
Sample Output 0

djkl
"""

s=input()
for i in range(len(s)):
    if s[i]!=s[len(s)-i-1]:
        break
print(s[i:len(s)-i])