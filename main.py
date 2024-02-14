from Dirichlet_Composition import *
from Reduce import *
from RBQF import *

def main():
### This code will print out the reduced forms of a discriminant -39
    bqfOfD(-39)
    print("_______________________")

### This code will print out the reduced forms of discriminants -3 up to -10
    bqfUpTo(-10)
    print("_______________________")

### This code will print out the reduced form that 3x^2+10xy+7y^2 is equivalent to
    print(reduce(3,10,7))
    print("_______________________")

### This code will print out the reduced form equivalent to the composition of 3x^2+3xy+4y^2 and 2x^2+xy+5y^2
    print(Dirichlet_Composition([3,3,4],[2,1,5]))
    print("_______________________")



main()