'''
Developer: Ömer ULUTÜRK
Date: 24.02.2021
Purpose of Software: Reinforcement of learned Python Code and Self-improvement


As a user, I want to use a program which can calculate the least common multiple (L.C.M.) of four numbers.
So that I can find the least common multiple (L.C.M.) of my inputs.

Acceptance Criteria:
Ask user to enter the four numbers. Use try/except blocks to verify input entries and warn the user for Nan or non numerical inputs.
Calculate the least common multiple (L.C.M.) of four numbers Use gcd function in module of math
'''

from math import gcd
import sys

def lcm(a,b,c,d):

    a = [a,b,c,d]  # will work for an int array of any length
    lcm = a[0]
    for i in a[1:]:
        lcm = lcm * i // gcd(lcm, i)
    print(lcm)
try:
    a=int(input("Please enter the first of the 4 numbers you want to find the lcm!"))
    b=int(input("Please enter the second of the 4 numbers you want to find the lcm!"))
    c=int(input("Please enter the third of the 4 numbers you want to find the lcm!"))
    d=int(input("Please enter the last of the 4 numbers you want to find the lcm!"))

    lcm(a,b,c,d)
except:
    print("Only integers are allowed")
    print(sys.exc_info()[0])