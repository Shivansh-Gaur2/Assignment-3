#QUESTION 6
#created a variable run to run loop again for entry of data
run = "Y"
#created a blank dictionary to store data
dict1 = dict()

while(run == "Y"):
    #asking user to enter his data
    sid = int(input("Enter your SID:- "))
    #storing his name by using sid as key
    dict1[sid] = str(input("Enter students name:- "))
    run = input("Do you want to more data Y or N:- ")
    run = run.upper()#to avoid conflict between Y and y

#PART A
print("Students details are as follows:- ", dict1)
#PART B
sortdict = sorted(dict1.items(), key=lambda x:x[1])
print("Sorted dictionary according to student name:- ", sortdict)

#PART C

print("Sorted dictionary accordind to SID:-" ,sorted(dict1.items()))
#PART D
print("Name:- " , dict1[int(input("Enter the SID:- "))])