

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
                coefs.append((a,b,int(c)))
                if(b != 0 and b < a):
                    coefs.append((a,-b,int(c)))
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
    
    if(d%2 == 0):
        d = d/2
        if(d%2 == 0):
            return False
    for i in range(3, int(abs(d)**0.5 + 1)):
        if d % i == 0:
            d = d / i

        if d % i == 0:
            return False
    return True


def main():
    d = -1
    while(d >= -200):
        #if(isFundamental(d)):
        classNumber = len(coefsOfBQF(d))
        print("h(" + str(d) + ") = " + str(classNumber) + " = " + str(coefsOfBQF(d)))
        d -= 1
    

main()