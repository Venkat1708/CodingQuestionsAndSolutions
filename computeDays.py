"""Kartik is a research scientist. He has developed a cure for zombies who have attacked the world. 
Now that everyone is under attack, it is time to distribute this cure efficiently to wipe out zombies from Earth. 
Though Kartik makes the cure, you are in charge of exporting the cure injections to the world

There are N countries (numbered 0 through N-1) in the world with populations A i >=1...A i-1 and everyone is infected to begin with. 
Each injection be used to are one infected person once.
Due to export regulations you may only export injections to one country per day, but you may choose any country that you want each day. 
On day 1, Kartik has x injections ready. On each subsed day, he can supply twice the number of injections that were delivered (ie, people that were cared) on the previous day.
Kartik cannot supply leftovers from the previous or any earlier day, as the medicine expires in a day.
Due to high demand from all countries, the maximum number of injections that you can export to a country an a given day will be the number of infected people in that country on that day.

However, zombles are not giving up so easily. 
They can infect a cured person that comes in contact with an infected person again-formally, 
it means that the number of infected people in a country doubles during the night, 
i.e after the cures for this day are used (maximum up to the population of that country).


For eg Country P with population 100 and country with population 20 country R with population 
40 Available number of injections to start is 20


Day 1: No injections were sent to country P and R. Let's assume 20 inject sent to

Day 2: Available supply of injections = 20 x 2 = 40. Infected in Country P=100 all 100 are still infected Country
 Q = All cured

Inected in Country R = 40people

Let's assume injections are sent to R. (40 can be sent as max supply is 40 o 23

Day Available supply of injections = 40 x 2=80 
infected in P = 100

Country Q = All cured 
Country R=All cured

Assuming injections are sent to P now (max 80 can be sent based on availabe supply)
so remaining infection in P=100-80-20

Day 4 Available supply of injections 80 x 2=160 
infected in P=20 x 2=40 (Infections doubled overnight after Day 3)
Country Q= All cured
Country R =All cured

Now p=40,but we have 160 Injections So Country P = All cured
Therefore number of days is 4


Input Specification:

input1: N (the number of countries) input2: x (number of injections available on the first day)

input3: A (array of integers indicating the population of the N counties

Output Specification:

Return the minimum number of days (integer).

Constraints:

1<=T <= 10^3

1 ≤N ≤ 10^5

1 ≤ a(i) ≤ 10^9 for each valid i

1≤ x ≤10^9

Example 1:

input 1: N =5

input 2: x = 5

input 3: A  = [1, 2, 3, 4, 5]
Output: 5

Example 2:

input 1: N=5 
input 2: x= 1

input 3: A=[40,30,20 10,50]

Output: 9
"""

def computeDays(input1,input2,input3):
    input3.sort()
    inject=input2
    count=0
    for i in input3:
        while(i>0):
            i=i-inject
            count+=1
            inject*=2
    return count   

print(computeDays(3,20,[100,20,40]))
