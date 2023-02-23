def silnia1(n):
    wynik = 1
    for i in range(1,n+1):
        wynik = wynik * i
    return wynik

def silnia2(n):
    if n == 1:
        return 1
    return n * silnia2(n-1)

def silnia3(n):
    def go(n, r):
        if n == 1:
            return r
        return go(n - 1, r * (n - 1))
    return go(n, n)


# print(silnia1(500))
# print(silnia2(500))
# print(silnia3(500))

def ciag_f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return ciag_f(n-1) + ciag_f(n-2)

print(ciag_f(40))

def ciag_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(n):
            c = a + b
            a = b
            b = c
        return a

print(ciag_fib(40))