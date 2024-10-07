def is_prime(func):
    def wraper(*args):
        result = func(*args)
        if result <= 1:
            res = 'Простое'
        if result == 2:
            res = 'Составное'
        if result % 2 == 0:
            res ='Составное'
        for i in range(3, int(result ** 0.5) + 1, 2):
            if result % i == 0:
                res ='Составное'
        res ='Простое'
        return res
    return wraper

@is_prime
def sum_three(*args):
    sum = 0
    for i in args:
        sum = sum + i
    print(sum)
    return sum

result = sum_three(2, 3, 6)
print(result)