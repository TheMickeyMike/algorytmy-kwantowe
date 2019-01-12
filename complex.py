import math


class ComplexNumber:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def add(self, liczba):
        return ComplexNumber(self.r + liczba.r, self.i + liczba.i)

    def subtrack(self, liczba):
        return ComplexNumber(self.r - liczba.r, self.i - liczba.i)

    def multiply(self, liczba):
        tempReal = self.r * liczba.r + -(self.i * liczba.i)
        tempImagine = (self.r * liczba.i) + (self.i * liczba.r)
        return ComplexNumber(tempReal, tempImagine)

    def divide(self, liczba):
        liczbaZobruconymZnakiem = liczba.conjugate()
        tempLicznik = self.multiply(liczbaZobruconymZnakiem)
        tempMianownik = liczba.multiply(liczbaZobruconymZnakiem)
        return ComplexNumber(tempLicznik.r / tempMianownik.r, tempLicznik.i / tempMianownik.r)

    def conjugate(self):
        return ComplexNumber(self.r, -self.i)

    def module(self):
        return ComplexNumber(math.sqrt(self.r ** 2 + self.i ** 2), 0)

    def __eq__(self, complex):
        if self.r == complex.r and self.i == complex.i:
            return True
        return False

    def qubit_repr(self):
        return f'{self.r}+{self.i}i'

    def __repr__(self):
        format = ''
        if self.r != 0:
            format += f'{self.r}'
            if self.i != 0:
                format += ' + '
        if self.i == 1:
            format += 'i'
        elif self.i != 0:
            format += f'{self.i}i'
        return format


class Vector:

    @staticmethod
    def add(v1, v2):
        wynik = []
        for idx, liczba in enumerate(v1):
            wynik.append(liczba.add(v2[idx]))
        return wynik

    @staticmethod
    def subtrack(v1, v2):
        wynik = []
        for idx, liczba in enumerate(v1):
            wynik.append(liczba.subtrack(v2[idx]))
        return wynik

    @staticmethod
    def scalar_multiply(scalar, v):
        wynik = []
        for idx, liczba in enumerate(v):
            wynik.append(liczba.multiply(scalar))
        return wynik

    @staticmethod
    def multiply(v1, v2):
        stack_to_sum = []
        for idx, zLiczba in enumerate(v1):
            stack_to_sum.append(zLiczba.multiply(v2[idx].conjugate()))
        sum = stack_to_sum[0]
        for idx, liczba in enumerate(stack_to_sum[1:]):
            sum = sum.add(liczba)
        return sum

    @staticmethod
    def norma(v1):
        stack_to_sum = []
        for idx, zLiczba in enumerate(v1):
            stack_to_sum.append(zLiczba.multiply(zLiczba.conjugate()))
        sum = stack_to_sum[0]
        for idx, liczba in enumerate(stack_to_sum[1:]):
            sum = sum.add(liczba)
        return '√{}'.format(sum)
