
# Predict the outcomes
#1
def a():
    return 5
print(a())

# Will print 5 on console.

#2
def a():
    return 5
print(a()+a())

#will print 10 on console.


#3
def a():
    return 5
    return 10
print(a())

#Will print 5

#4
def a():
    return 5
    print(10)
print(a())

#will print 5

#5
def a():
    print(5)
x = a()
print(x)

#will print 5 once and then print none because nothing is returned by the funtion

#6
def a(b,c):
    print(b+c)
# print(a(1,2) + a(2,3))

#Will print 3 and 5 but then crash as nothing is returned


#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))


#Will print 25


#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())
#Will print 100 and then print 10

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))  #will print 7
print(a(5,3))  #will print 14
print(a(2,3) + a(5,3)) #will print 21


#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))       #will print 8


#11
b = 500
print(b)   #will print 500
def a():
    b = 300
    print(b)
print(b) #will print 500
a()     #will print 300
print(b) #will print 500

#12
b = 500
print(b) #Will print 500
def a():
    b = 300
    print(b)
    return b
print(b)    #Will print 500
a()         #Will print 300
print(b)    #Will print 500


#13
b = 500
print(b)    #Will print 500
def a():
    b = 300
    print(b)
    return b
print(b)    #Will print 500
b=a()       #Will print 300
print(b)    #Will print 300


#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a() #Will print 1, 3, 2


#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)  #WILL PRINT 1, 3, 5, 10
