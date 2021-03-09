# Basic - Print all the numbers/integers from 0 to 150.

for count in range(0, 151):
    print(count)


# Multiples of Five - Print all the multiples of 5 from 5 to 1,000,000.

for count in range(0, 1000001):
    if( count % 5 == 0):
        print(count)


# Counting, the Dojo Way - Print integers 1 to 100.  If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".
for count in range(1, 101):
    if count % 10 == 0:
        print("Dojo")
    elif count % 5 == 0:
        print("Coding")
    else:
        print(count)



# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
final_sum = 0
for count in range(0, 500001):
    if count % 2 != 0:
        final_sum += count
print("Final Sum: {}".format(final_sum))
print(f"Final sum: {final_sum}")



# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours (exclude 0).
counter = 2018
while counter > 0:
    print(counter)
    counter -= 4



# Flexible Countdown - Based on earlier "Countdown by Fours", given lowNum, highNum, mult, print multiples of mult from lowNum to highNum, using a FOR loop.  For (2,9,3), print 3 6 9 (on successive lines)
lowNum = 10
highNum = 50
mult = 5
for count in range(10, 51):
    if count % mult == 0:
        print(count)
