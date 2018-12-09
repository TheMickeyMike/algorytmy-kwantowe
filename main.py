from complex import ComplexNumber, Vector
#
# Wektory
#
print(f'{"#" * 5} WEKTORY {"#" * 5}')

W = [ComplexNumber(1, 2), ComplexNumber(3, -4)]
V = [ComplexNumber(-1, -1), ComplexNumber(2, 1)]


# Dodawanie
print(f'Dodawanie: {[m for m in Vector.add(W, V)]}')

# Odejmowanie
print(f'Odejmowanie: {[m for m in Vector.subtrack(W, V)]}')

# Monożenie wektora przez skalar
print(
    f'Monożenie wektora przez skalar: {[m for m in Vector.scalar_multiply(ComplexNumber(1, 1), V)]}')

# Mnożenie wektora
print(f'Mnożenie wektora: {Vector.multiply(V, W)}')
print(f'Mnożenie wektora: {Vector.multiply(W, V)}')

# Norma
H = [ComplexNumber(1, 1), ComplexNumber(3, -1)]  # 2√3 = √12
# H = [ComplexNumber(0, 1), ComplexNumber(0, 0)] # √1 = 1 => wektor unormowany
print(f'Norma wektora: {Vector.norma(H)}')


#
#   Liczby zespolone
#
print(f'\n{"#" * 5} Liczby zespolone {"#" * 5}')
# Dodawanie
print(f'Dodawanie: {ComplexNumber(2, 3).add(ComplexNumber(1, 2))}')

# Odejmowanie
print(f'Odejmowanie : {ComplexNumber(2, 3).subtrack(ComplexNumber(1, 2))}')

# Mnożenie
print(f'Mnożenie: {ComplexNumber(2, 3).multiply(ComplexNumber(2, 2))}')

# Dzielenie
print(f'Dzielenie: {ComplexNumber(1, 5).divide(ComplexNumber(1, 3))}')

# Sprzężenie
print(f'Sprzężenie: {ComplexNumber(2, 3).conjugate()}')

# Moduł
print(f'Moduł: {ComplexNumber(2, 2).module()}')
