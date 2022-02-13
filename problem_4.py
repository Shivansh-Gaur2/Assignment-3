#QUESTION 4
#created variable to store value of performance
performance = str()
#created variable to run code again
run =  "y"
while(run == "y"):
    grade = int(input("Enter your grade:- "))
    #Checking grades are between 4 and 10
    if(grade<4):
        print("Grade is out of range")
    #created different conditions and stored values according to question
    elif(grade==4):
        performance = "Poor"
        grade = "D"
    elif(grade==5):
        performance = "Below Average"
        grade = "C"
    elif(grade == 6):
        performance = "Average"
        grade = "C+"
    elif(grade == 7):
        performance = "Good"
        grade = "B"
    elif(grade == 8):
        performance = "Very Good"
        grade = "B+" 
    elif(grade == 9):
        performance = "Excellent"
        grade = "A"
    elif(grade == 10):
        performance = "Outstanding"
        grade = "A+"
    print(f"Your Grade is '{grade}' and {performance} Performance")        
    run = str(input("do you want to run again Y or N:- "))
    run = run.lower() #to avoid conflict between Y and y                       
    