from decimal import Decimal


def wydaj_reszte(reszta):
    nominal = [Decimal(5), Decimal(2), Decimal(1), Decimal('0.5'), Decimal('0.2'), Decimal('0.1'), Decimal('0.05'),
               Decimal('0.02'), Decimal('0.01')]
    do_wydania = []
    while reszta > 0:
        for n in nominal:
            if n <= reszta:
                do_wydania.append(n)
                reszta -= n
                break
    return do_wydania


print(wydaj_reszte(Decimal('.33')))

a = (1,2,3,4,5)

(s,d,f,g,h)= a

print(a[0])