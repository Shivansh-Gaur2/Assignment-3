#QUESTION 6
#defining number of rows for pattern
rows = 6
for i in range(rows):
    # created loop to print spaces
    for j in range(i):
        print(' ', end='')
    # created loop to print alphabets
    for j in range(2*(rows-i)-1):
        print(chr(65 + j), end='')
    #created blank print to shift to next row
    print()