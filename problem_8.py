#QUESTION 8
#creating sets given in question
set1  = {1,2,3,4,5}
set2 = {2,4,6,8}
set3 = {1,5,9,13,17}
#PART A
#Create a new set of all elements that are in Set1 and Set2 but not both.
 #symmetric_difference will union of elements in both and remove duplicate elements
seta = (set1.symmetric_difference(set2))
print("SET A is given by:- " , seta)
#PART B
#Create a new set of all elements that are in only one of the three sets Set1,
#Set2 and Set3.
setb = set1.symmetric_difference((set2.symmetric_difference(set3)))
print(" SET B is given by:- ",setb)

#PART C
#Create a new set of elements that are exactly two of the sets Set1, Set2
#and Set3.
setc = set1.intersection(set2).union(set1.intersection(set3))
print("SET C is given by:- ",setc)

#PART D
#Create a new set of all integers in the range 1 to 10 that are not in Set1.
#created a new set of all integers in the range 1 to 10
setall = {1,2,3,4,5,6,7,8,9,10}
setd = set1.symmetric_difference(setall)
print("SET D is given by:- ",setd)
#PART E
# Create a new set of all integers in the range 1 to 10 that are not in Set1,
#Set2 and Set3.
'''taking symmetric difference of set1 ,2 and 3 with setall to remove duplicate elements then taking 
intersection of sets to get elements which are not in set1,2,3'''

sete = setall.symmetric_difference(set1).intersection(setall.symmetric_difference(set2)).intersection(setall.symmetric_difference(set3))
print("SET E is given by:- ",sete)