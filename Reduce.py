
def reduce(a,b,c):
    discriminant = b**2-4*a*c
    if (discriminant > 0):
        return "Error: The discriminant is positive."
    if c<a:
        return reduce(c,-b,a)
    elif (b>a or b<= -a):
        B = b%(2*a)
        try:
            assert (-a < B and B <= a)
        except:
            B = b%(2*-a)
            assert (-a < B and B <= a)
        k = (b-B)/(2*a)
        return reduce(a,B,(a*(k)**2)-(b*k)+c)
    elif (c==a and -a < b <0):
        assert(0 <-b < a)
        return reduce(a,-b,a)
    return [int(a), int(b), int(c)]

