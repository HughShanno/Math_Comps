import math
from Reduce import reduce
from sympy.solvers.diophantine import diophantine
from sympy import symbols

x, y, z, t_0, t_1 = symbols("x, y, z, t_0, t_1", integer=True)
def Dirichlet_Composition(f1,f2):
    if (f1[0] == f2[0]):
        temp = f1[0]
        f1[0] = f1[2]
        f1[1] = -f1[1]
        f1[2] = temp
    a1 = f1[0]
    b1 = f1[1]
    c1 = f1[2]
    a2 = f2[0]
    b2 = f2[1]
    d= b1**2-4*a1*c1
    d2 = b2**2-4*a2*f2[2]
    if(d != d2):
        return "Error: Please imput forms of the same Discriminant."

    e = math.gcd(a1,a2,int((b1+b2)/2))
    solution = diophantine(int((a1/e))*x+int((a2/e))*y+int(((b1+b2)/(2*e)))*z -1)
    for element in solution:
        solution = element
    coefs = []
    for i in range(len(solution)):
        coefs.append(int(solution[i].evalf(subs={t_0:2, t_1:3})))
    if(len(coefs) == 2):
        coefs.append(-1)
    B = (coefs[0]*a1*b2)/e+(coefs[1]*a2*b1)/e+(coefs[2]*(b1*b2+d)/(2*e))
    return reduce(int((a1*a2)/e),int(B),int((e**2*(B**2-d))/(4*a1*a2)))