"""
The positive even numbers are sorted in ascending order as 2, 4, 6, 8, 10, 12, 14, 16 ……, and grouped as (2), (4, 6), (8, 10, 12), (14, 16, 18, 20) and so on. Thus, the first group is (2), the second group is (4, 6), the third group is (8, 10, 12), etc. In general, the kth group contains the next k elements of the sequence. Given k, find the sum of the elements of the kth group.

Input: First line will contain T, number of testcases. Next T lines have a single integer k for each testcase. Output: Print the sum of elements in the kth group in each testcase separated by line break.

Constraints 1≤T≤50 1≤k≤106 Sample Input: 2 3 5 Sample Output: 30 130 EXPLANATION: Case 1: For k=3, the 3rd group has (8, 10, 12). So, 8+10+12=30. Case 2: For k=5, the 5th group has (22, 24, 26, 28, 30). So, 22+24+26+28+30=130.
"""

t=int(input())
for i in range(t):
    n=int(input())
    l=list(range(2,(n**2)+(n+1),2))
    temp=[]
    for j in range(n):
        temp.append(l[0:(j+1)])
        k=j
        while(k!=-1):
            l.pop(0)
            k=k-1
    print(sum(temp[n-1]))
##printing the squence
print("List printing")
print(temp)