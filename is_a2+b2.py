
def is_ab(n):
    squares = set()

    i = 0

    while i**2 <= n:
        squares.add(i**2)
        i += 1

    for square in squares:
        if n-square in squares:
            return (square, n-square)
    return False

print(is_ab(126))