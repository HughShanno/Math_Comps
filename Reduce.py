
def reduce(a,b,c):
    if c<a:
        return reduce(c,-b,a)
    elif (b>a or b<= -a):
        B = abs(b)%(2*a)
        assert (-a < B and B <= a)
        k = (b-B)/(2*a)
        return reduce(a,B,(a*k**2)-(b*k)+c)
    elif (c==a and -a < b <0):
        assert(0 <-b < a)
        return reduce(a,-b,a)
    return [int(a), int(b), int(c)]


def main():
    print(str(reduce(2, -1 ,3)))

main()