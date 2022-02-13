#QUESTION 3
list1 = list()#Creating a blank list 
num = int(input("Enter the number of elements you want to enter in list:- "))#asking user for number of elements in list
i = 1 #assigned value 1 to variavle i
#creating a loop to ask user for element whose square needs to be shown
while(i<=num):
    list1.append(int(input(f"Enter {i} element:- ")))
    i+=1
list2 = list()#creating a blank list
for i in list1:
    tup = (i,i**2)
    list2.append(tup)#adding tuple to list
print(list2)    
