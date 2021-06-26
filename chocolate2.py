"""
A chocolate company came up with an offer for their 100 years anniversary. They have introduced two new chocolate packets. The first pack contains 1000chocolates and costs ₹500 and the other pack of 5chocolates costs ₹5. (These are the only packs sold by the company) Aditya has X rupees. Help Aditya to find the maximum number of chocolates he can buy with the available money.

Input: A single integer X Output: The maximum number of chocolates Aditya can buy in ₹X.

Constraints 0≤X≤109 X is an integer.

Sample Input: 1024 Sample Output: 2020 EXPLANATION: Aditya can buy 2 packs of 1000 chocolates which will cost him 500x2=1000. Then he can buy 4 packs of 5 chocolates that will cost him 5x4=20. So, the total number of chocolates he will have is 2000+20=2020

"""

n=int(input())
nc=0
if n>=500:
    nc=(n//500)*1000
    n=n%500
    if n==0:
        print(nc)
    else:
        nc=nc+(n//5)*5
        print(nc)
else:
    nc=(n//5)*5
    print(nc)#choclate count