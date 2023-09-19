from prime_factorization import find_prime_factors
import math


def is_sum_of_squares_proper_approach(n):
    squares = set()

    i = 0

    while i**2 <= n:
        squares.add(i**2)
        i += 1

    for square in squares:
        if n-square in squares:
            return (int(square**(0.5)), int((n-square)**(0.5)))
    return 'Cannot be represented'

def is_sum_of_squares(n):
    decomposition = find_prime_factors(n+1)
    sum_of_squares = True
    for key, val in decomposition[n].items():
        if key%4 == 3 and val%2:
            sum_of_squares = False
    return sum_of_squares

def to_csv(n):
    with open(str(n)+'_prime_decompsition.csv', 'w') as fout:
        decomposition = find_prime_factors(n+1)
        i = 2
        for factorization in decomposition[2:]:
            to_write = str(i) + ','
            for key in sorted(factorization.keys()):
                to_write += str(key) + '^' + str(factorization[key]) + ' * '
            to_write = to_write[:-3]
            to_write += ','
            to_write += '"' + str(is_sum_of_squares_proper_approach(i)) + '"' + '\n'
            fout.write(to_write)
            i += 1


to_csv(1000)