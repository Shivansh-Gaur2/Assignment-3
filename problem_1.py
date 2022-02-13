#QUESTION 1
#asking user if he wants to enter word or string
var = input("Do you want to enter string or word? ")
if(var == "string"):
    string = input("Enter the string:- ")
    dict1 = dict() #creating a blank dictionary to add values
    words = string.split() #splitting words of sentence and storing them
    for word in words:
        if word in dict1:
            dict1[word] +=1 #if word is in dictionary increment by 1
        else:
            dict1[word] = 1 #if not in dictionary value = 1   
    print(dict1)     
elif(var == "word"):
    string = input("Enter the word:- ")
    dict1 = dict()
    char = string[:]    #splitting characters of word
    for ch in char:
        if ch in dict1:
            dict1[ch] +=1 #if character is in dictionary increment by 1
        else:
            dict1[ch] = 1 #if not then value = 1
    print(dict1)               