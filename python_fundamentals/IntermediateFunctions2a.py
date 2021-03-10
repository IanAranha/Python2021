x = [ [5,2,3], [10,8,9] ]

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

z = [ {'x': 10, 'y': 20} ]


# How would you change the value 10 in x to 15?  Once you're done x should then
# be [ [5,2,3], [15,8,9] ].

print(x)
x[1][0] = 15
print(x)

# How would you change the last_name of the first student from 'Jordan' to
# "Bryant"?

print(students)
students[0]["last_name"]="Bryant"
print(students)

# For the sports_directory, how would you change 'Messi' to 'Andres'?
print(sports_directory)
print(sports_directory["soccer"][0])
sports_directory["soccer"][0] = "Andres"
print(sports_directory)
print(sports_directory["soccer"][0])

# For z, how would you change the value 20 to 30?
print(z)
print(z[0])
print(z[0]["y"])
z[0]["y"]=30
print(z)
print(z[0])
print(z[0]["y"])
