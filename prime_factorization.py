n = 127

seive = [i for i in range(n)]
decomposition = [{} for i in range(n)]

i = 2
for num in seive[2:]:
    if i == num:
        j = i
        while j < len(seive):
            while seive[j]%num == 0:
                seive[j] /= num
                decomposition[j][num] = decomposition[j].get(num,0)+1
            j += num
    i += 1

i = 2
for factorization in decomposition[2:]:
    print(i, ':', end = ' ')
    for key in sorted(factorization.keys()):
        print('(' + str(key) + '^' + str(factorization[key]) + ')', end = '')
    print('')
    i += 1

