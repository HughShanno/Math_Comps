def find_prime_factors(n): # pass in 1 number higher than you actually need
    seive = [i for i in range(n)]
    decomp = [{} for i in range(n)]

    i = 2
    for num in seive[2:]:
        if i == num:
            j = i
            while j < len(seive):
                while seive[j]%num == 0:
                    seive[j] /= num
                    decomp[j][num] = decomp[j].get(num,0)+1
                j += num
        i += 1
    return decomp



