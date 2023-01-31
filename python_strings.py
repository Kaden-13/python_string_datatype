# TODO Create Variables
#   - Create the following variables

#   - my_first_name
#       -set this equal to your first name
myFirstName = 'Kaden'
#   - my_last_name
#       -set this equal to your last name
myLastName = "Donaldson"
#   - my_year_of_birth
#       -set this equal to your birth year (doesn't have to be real should be less then 100 yrs ago)
myYearOfBirth = 2003
#   - current_year
#       -set this equal to 2023
currentYear = 2023





# TODO String Indexing
#   - Print the following items (one per line) (print using variables)
#       - first name  
print(myFirstName)
#       - last name
print(myLastName)
#       - first letter of your first name (use the +index)
print('First letter of first name:', myFirstName[0])
#       - second letter of your last name (use the -index)
print("Second letter of last name:", myLastName[-8])
#       - first two letter of your first name (use the +index)
print("First two letters of first name:", myFirstName[0:2])
#       - second two letter of your last name (use the -index)
print("Second two letters of last name:", myLastName[-2:])





# TODO Combining Strings
#   - Print the following items (one per line) (print using variables)
#       -first name and last name combined
print(myFirstName, myLastName) #CONCATINATION
#       -first name six times
for i in range (6):
    print(myFirstName)




# TODO Formatting Strings
#   - Print the following items (one per line) (print using variables)
#       - first name last name -was born in- year of birth
print(myFirstName, myLastName, "was born in", myYearOfBirth)
#       - first name last name -was born in- year of birth. first name -enjoyed celebrating- current year
print(myFirstName, myLastName, "was born in", myYearOfBirth, myFirstName, "enjoyed celebrating", currentYear)


# TODO Escape characters
#   - Print the following items (one per line) (print using variables)
#       - possesive first name -birth year is- year of birth 
print(myFirstName, "birth year is", myYearOfBirth)
#       - tab last name current year
print("",myLastName, currentYear)

# TODO String methods
#   - Print the following items (one per line) (print using variables)
#       - first name and last name in lower case
print(myFirstName.casefold(), myLastName.casefold())
#       - length of last name
print(myLastName.__len__())
#       - first name and last name all in upper case
print(myFirstName.upper(), myLastName.upper())