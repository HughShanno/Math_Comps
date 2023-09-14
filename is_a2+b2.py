from prime_factorization import find_prime_factors


def is_sum_of_squares_proper_approach(n):
    squares = set()

    i = 0

    while i**2 <= n:
        squares.add(i**2)
        i += 1

    for square in squares:
        if n-square in squares:
            return (square, n-square)
    return False

def is_sum_of_squares(n):
    decomposition = find_prime_factors(n+1)
    sum_of_squares = True
    for key, val in decomposition[n].items():
        if key%4 == 3 and val%2:
            sum_of_squares = False
    return sum_of_squares



print(is_sum_of_squares_proper_approach(126))