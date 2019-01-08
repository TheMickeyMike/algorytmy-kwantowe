import numpy as np


class QGate:
    def __init__(self, matrix):
        self.matrix = matrix


H = QGate(np.matrix([[1, 1], [1, -1]], dtype=np.complex64)
          * (1.0 / np.sqrt(2)))
X = QGate(np.matrix([[0, 1], [1, 0]], dtype=np.complex64))
Y = QGate(np.matrix([[0, -1j], [1j, 0]], dtype=np.complex64))
Z = QGate(np.matrix([[1, 0], [0, -1]], dtype=np.complex64))


class Qubit:
    def __init__(self, zero_prob, one_prob):
        assert abs(complex(zero_prob)) ** 2 + abs(complex(one_prob)
                                                  ) ** 2 == 1, 'Nie spełnia warunku: |α|^2 + |β|^2 = 1'
        self.zero_propability = complex(zero_prob)
        self.one_propability = complex(one_prob)
        self._zero_ket = self.zero_propability * np.matrix([[1], [0]])
        self._one_ket = self.one_propability * np.matrix([[0], [1]])
        self.value = self._zero_ket + self._one_ket

    def __repr__(self):
        return f'{self.value}'

    def apply(self, gate):
        self.value = gate.matrix * self.value


# qb = Qubit(1, 0)  # Qubit value 0
# print(qb)
# print(qb.apply(X))
# print(qb)

# qb = Qubit(1, 0)  # Qubit value 0
# print(qb)
# print(qb.apply(Y))
# print(qb)

# qb = Qubit(0, 1)  # Qubit value 0
# print(qb)
# print(qb.apply(Z))
# print(qb)

qb = Qubit(1, 0)  # Qubit value 0
print(qb)
print(qb.apply(H))
print(qb)
