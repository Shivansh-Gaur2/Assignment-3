date = int(input("Enter the date(1,31):- "))
month = int(input("Enter the month(1,12):- "))
year = int(input("Enter the year(1800,2025):- "))
days = int()
#checking conditions for leap year
if(((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
     leap_year  = True
else:
     leap_year = False
#checking conditions to define number of days in month is 28,29,30 or 31
if month in (1,3,5,7,8,10,12):
    days = 31
elif (month ==2):    
    if leap_year == True:
        days = 29
    else:
        days = 28    
else:
    days = 30    
#checking if it is last day of month     
if(days == date):
    #created conditions for next day 
    if(month ==2):
        if(date == 28):
            date = 29
        elif(date == 29):
            date = 1
            month += 1       
    elif(month== 12):
        month = 1
        date = 1
        year += 1 
    else:
        date = 1
        month += 1  
#if it is not the last day of month               
elif(date < days):
    date += 1
                
print(f"next date is {date}/{month}/{year}")                    