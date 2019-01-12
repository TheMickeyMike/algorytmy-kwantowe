from complex import ComplexNumber
import numpy as np


class QGate:
    def __init__(self, matrix):
        self.matrix = matrix


X = QGate(np.matrix([
    [ComplexNumber(0, 0), ComplexNumber(1, 0)],
    [ComplexNumber(1, 0), ComplexNumber(0, 0)]
]))


class Qubit:
    def __init__(self, zero_prob: ComplexNumber, one_prob: ComplexNumber):
        assert zero_prob.module().multiply(zero_prob).add(one_prob.module().multiply(
            one_prob)) == ComplexNumber(1, 0), 'Nie spełnia warunku: |α|^2 + |β|^2 = 1'
        self.zero_prob = zero_prob
        self.one_prob = one_prob

        # assert abs(complex(zero_prob)) ** 2 + abs(complex(one_prob)
        #                                           ) ** 2 == 1, 'Nie spełnia warunku: |α|^2 + |β|^2 = 1'

    def __repr__(self):
        return str(self.zero_prob.qubit_repr()) + "|0>  +  " + str(self.one_prob.qubit_repr()) + "|1>\n"

    def apply(self, gate):
        self.value = gate.matrix * self.value


q = Qubit(ComplexNumber(1, 0), ComplexNumber(0, 0))
print(q)
print(q.apply(X))
