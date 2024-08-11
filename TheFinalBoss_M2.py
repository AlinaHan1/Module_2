import random
def number():
    j = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    n = random.choice(j)
    return n


n = number()
#print(n)
res = ''
for i in range(1, n):
    for b in range(i + 1, n):
        if n % (i + b) == 0:
            res += str(i)
            res += str(b)
print(n, '-', res)
