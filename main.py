# Answers:

#1.
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(raw_input().strip())
    if (n % 2 == 1):
        print("Weird")
    elif (n >= 2 and n <= 5 or n > 20):
        print("Not Weird")
    else:
        print ("Weird")

#2.
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

#3.
    print(a//b) #Results in integer division
    print(a/b)  #Results in float division

#4.
    for i in range(n):
        print(i*i)

#5.
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4 == 0:
      if(year%100 != 0 or year%400 == 0):
         leap = True
    
    return leap

year = int(input())
print(is_leap(year))

#6.
