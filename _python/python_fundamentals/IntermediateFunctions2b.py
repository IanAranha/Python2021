# Create a function that given a list of dictionaries, it loops through each dictionary in the list and prints each key and the associated value.  For example, given the following list:
#
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
# iterateDictionary( students ) should output
#
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# for i in range(0, len(students)):
#     print(students[i])


# for i in range(0, len(students)):
#     result = "".join([key + " - " + val + " "for key, val in students[i].items()])
#     print(result)

# Creating a function of the code above so it works with any list of dictionaries

def dictIteration(list):
    for i in range(0, len(list)):
        result = "".join([key + " - " + val + ", " for key, val in list[i].items()])
        print(result)

dictIteration(students)




# Create a function that given a list of dictionaries and a key name, it
# outputs the value stored in that key for each dictionary.  For example, iterateDictionary2('first_name', students) should output:
# Michael
# John
# Mark
# KB

# for i in range(0, len(students)):
#     print(students[i]["first_name"])
#
#
# #Now making the above code into a function
def dictIteration2(key, list):
    for i in range(0, len(list)):
        print(students[i][key])
#
dictIteration2("first_name", students)
dictIteration2("last_name", students)


# Say that
#
dojo = {
        'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC',
                'Burbank'],
        'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham',
                'Patrick', 'Minh', 'Devon']
    }
# Create a function that prints the name of each location and also how many
# locations the Dojo currently has.
# Have the function also print the name of each instructor and
# how many instructors the Dojo currently has.
#
# For example, printDojoInfo(dojo) should output
#
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
#
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

# for key, val in dojo.items():
#     print("".join([str(len(dojo[key])) + " " + key.upper()]))
#     for i in range(0, len(val)):
#         print(val[i])

#Putting the code into a function

def printingDojoInformation(dict):
    for key, val in dict.items():
        print("".join([str(len(dict[key])) + " " + key.upper()]))
        for i in range(0, len(val)):
            print(val[i])
        print("\n")

printingDojoInformation(dojo)
