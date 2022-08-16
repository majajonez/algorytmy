# def silnia1(n):
#     wynik = 1
#     for i in range(1,n+1):
#         wynik = wynik * i
#     return wynik
#
# def silnia2(n):
#     if n == 1:
#         return 1
#     return n * silnia2(n-1)
#
#
#
# print(silnia2(5))

def ciag_f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return ciag_f(n-1) + ciag_f(n-2)

print(ciag_f(5))