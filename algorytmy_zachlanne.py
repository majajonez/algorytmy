from decimal import Decimal


def pay_the_rest(rest):
    denomination = [Decimal(5), Decimal(2), Decimal(1), Decimal('0.5'), Decimal('0.2'), Decimal('0.1'), Decimal('0.05'),
               Decimal('0.02'), Decimal('0.01')]
    to_be_paid = []
    while rest > 0:
        for n in denomination:
            if n <= rest:
                to_be_paid.append(n)
                rest -= n
                break
    return to_be_paid


print(pay_the_rest(Decimal('.33')))

a = (1,2,3,4,5)

(s,d,f,g,h)= a

print(a[0])