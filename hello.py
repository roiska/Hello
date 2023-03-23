whatup = "whatup world"
print(whatup)
print(len(whatup))

if len(whatup) < 4:
    print("short")
else:
    print("long")

fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print(len(x))


lowNumbers = []


def printRange(endrange):
    for item in range(1,endrange):
        if (item < 34):
            lowNumbers.append(item) 
        # end if 
    print(lowNumbers[4])
# end def


printRange(67)