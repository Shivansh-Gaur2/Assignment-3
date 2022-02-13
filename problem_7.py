#QUESTION 7
'''Write a python program to print Fibonacci sequence also print average of the
resultant Fibonacci series.'''
#created variable num1 and num2 as starting numbers of fibonacci
#created variable sums to calculate summation of numbers in fibonacci
#creater variable total to calculate number of terms in fibonacci
from unittest.util import strclass


num1,num2,sums,total = 0,1,0,0
#asking user for input 
num = int(input("Enter number:- "))
#created while loop with condition to run till num1 is less than num
while(num1<num):
    #taking output of terms of fibonacci
    print(num1 , end = ' ')#used end = ' ' to avoid creating new line
    sums = sums + num1 #adding terms to summation to get total of all terms
    num1, num2 = num2,num1+num2 #reasssigned value to get next term of series
    total += 1
print()#to create a new line
print("Average of terms is:- " + str(sums/total)) #printed average 