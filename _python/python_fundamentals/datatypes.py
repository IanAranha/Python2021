#Storing a string in a variable
#variable = name
#data type = string = "Ian Aranha"

name = "Ian Aranha"



#Storing an integer

age = 54



#Storing a float

weight = 220.3



#Storing a boolean
hearing = False



#Storing a list (Also called array - but List in python)

ninjas = ["Rozen", "KB", "Oliver"]



#Storing a dictionary

new_person = { "name": "John", "age" : 35, "weight" : 184 , "hearing" : True }



#Storing different data types in a List

myList = [ '4', ["list", "within", "a", "list"], 987]

emptyList = []


#Data manipulation
print(ninjas[0])    #Prints Rozen
print(ninjas[1])    #Prints KB
print(ninjas[2])    #Prints Oliver
print(len(ninjas))  #Prints lenght of list

ninjas.append("Michael")
print(len(ninjas))
print(ninjas[0])
print(ninjas[1])
print(ninjas[2])
print(ninjas[3])



ninjas.pop()
print(ninjas[0])
print(ninjas[1])
print(ninjas[2])



ninjas.pop(1)
print(len(ninjas))
print(ninjas[0])
print(ninjas[1])


#Update an element in the list --> overwrite
ninjas[1] = "John Armand"
print(ninjas[0])
print(ninjas[1])
