numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes_ = []
not_primes = []
for i in numbers:
   #   print(i)
        if i < 2:
            continue
        for j in range(2, i):
            if i % j == 0:
                not_primes.append(i)
                break
        else:
                primes_.append(i)
print(primes_)
print(not_primes)