from Reduce import reduce

def coefsOfBQF(d):
    if(d%4 == 3 or d%4 == 2):
        return []
    sqrtD = (abs(d)/3)**0.5
    a = 1
    coefs = []
    while(a <= sqrtD):
        b = 0
        while (b <= a):
            c = (b**2 -d)/(4*a)
            if(c.is_integer()):
                reducedList = reduce(a,b,c)
                if (a == reducedList[0] and b == reducedList[1] and c == reducedList[2]):
                    coefs.append((int(a),int(b),int(c)))
                    reducedList2 = reduce(a,-b,c)
                    if(reducedList2 != reducedList):
                        coefs.append((int(a),int(-b),int(c)))
            b += 1
        a += 1
    return coefs

def displayBQFS(coefs):
    length = len(coefs)
    for i in range(length):
        print(str(coefs[i][0])+"x^2 + "+ str(coefs[i][1])+"xy + "+ str(coefs[i][2])+"y^2")

# add a checker for fundamental discriminants.

def isFundamental(d):
    if(d%4 == 3 or d%4 == 2):
        return False
    if (d%4 == 0):
        d = d/4
        if(d%4 == 0 or d%4 == 1):
            return False
    
    #check if it's divisible by 4
    if(d%2 == 0):
        d = d/2
        if(d%2 == 0):
            return False
    #to check the rest of the squares we only need to check up to sqrt(d), so look for the numbers that divide d
    # and check if you can divide d twice by them, if you can, then it's not fundamental.
    for i in range(3, int(abs(d)**0.5 + 1)):
        if d % i == 0:
            d = d / i

        if d % i == 0:
            return False
    return True


def main():
    d = -1
    while(d >= -100):
        coefs = coefsOfBQF(d)
        for list in coefs:
            assert(-list[0] < list[1] <= list[0] <= list[2])
            if(list[0] == list[2]):
                assert(list[1] >= 0)
        classNumber = len(coefs)
        if(isFundamental(d)):
            print("h(" + str(d) + ") = " + str(classNumber) + " = " + str(coefs))
        elif(d % 4 == 3 or d % 4 == 2):
            pass
        else:
            print("h(" + str(d) + ") = " + str(classNumber) + " = " + str(coefs)+ " Not Fundamental")
        d -= 1


main()