

def coefsOfBQF(d):
    sqrtD = (abs(d)/3)**0.5
    a = 1
    coefs = []
    while(a <= sqrtD):
        b = 0
        while (b <= a):
            c = (b**2 -d)/(4*a)
            if(c.is_integer()):
                coefs.append((a,b,int(c)))
                #if(b != 0):
                    #coefs.append((a,-b,int(c)))
            b += 1
        a += 1
    return coefs

def displayBQFS(coefs):
    length = len(coefs)
    for i in range(length):
        print(str(coefs[i][0])+"x^2 + "+ str(coefs[i][1])+"xy + "+ str(coefs[i][2])+"y^2")

def main():
    d = -1
    while(d >= -171):
        classNumber = len(coefsOfBQF(d))
        print("h(" + str(d) + ") = " + str(classNumber) + " = " + str(coefsOfBQF(d)))
        d -= 1
    #displayBQFS(coefsOfBQF(-4))
main()