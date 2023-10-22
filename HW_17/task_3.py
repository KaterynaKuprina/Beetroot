def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        new_func = gcd(new_numerator, new_denominator)
        return Fraction(new_numerator // new_func, new_denominator // new_func)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        new_func = gcd(new_numerator, new_denominator)
        return Fraction(new_numerator // new_func, new_denominator // new_func)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        new_func = gcd(new_numerator, new_denominator)
        return Fraction(new_numerator // new_func, new_denominator // new_func)


    def __truediv__(self, other):
        assert other.numerator != 0
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        new_func = gcd(new_numerator, new_denominator)
        return Fraction(new_numerator // new_func, new_denominator // new_func)

    def __eq__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return new_numerator == new_denominator






x = Fraction(1, 2)
y = Fraction(1, 4)
print(type(Fraction(3, 4)))
print(type(x + y))
print(x * y)
print(x - y)
print(x / y)



if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    print(x + y == Fraction(3, 4))