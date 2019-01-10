from numpy import matrix
from numpy import linalg
import numpy
import math
import random


class Qubit:
    def __init__(self, a, b):
        assert abs(complex(a)) ** 2 + abs(complex(b)
                                          ) ** 2 == 1, 'Nie spełnia warunku: |α|^2 + |β|^2 = 1'
        self.zero = complex(a)
        self.one = complex(b)

    def xgate(self):
        '''Apply a NOT (X) gate'''
        x = matrix([
            [0, 1],
            [1, 0]
        ])
        curr = matrix([[self.zero], [self.one]])
        new = numpy.asarray(x * curr)
        self.zero = new[0][0]
        self.one = new[1][0]
        return self

    def ygate(self):
        '''Apply a (Y) gate'''
        y = matrix([
            [0, -1j],
            [1j, 0]
        ], dtype=numpy.complex64)
        curr = matrix([[self.zero], [self.one]])
        new = numpy.asarray(y * curr)
        self.zero = new[0][0]
        self.one = new[1][0]
        return self

    def zgate(self):
        '''Apply a (Z) gate'''
        z = matrix([
            [1, 0],
            [0, -1]
        ], dtype=numpy.complex64)
        curr = matrix([[self.zero], [self.one]])
        new = numpy.asarray(z * curr)
        self.zero = new[0][0]
        self.one = new[1][0]
        return self

    def hgate(self):
        '''Apply a Hadamard gate'''
        h = numpy.multiply((1.0 / numpy.sqrt(2)), matrix([
            [1, 1],
            [1, -1]
        ], dtype=numpy.complex64))
        curr = matrix([[self.zero], [self.one]])
        new = numpy.asarray(h * curr)
        self.zero = new[0][0]
        self.one = new[1][0]
        return self

    def measure(self):
        '''Measure the qubit in the computational basis'''
        zeroprob = abs(self.zero) ** 2
        randomchoice = random.random()

        if randomchoice < zeroprob:
            self.zero = complex(1)
            self.one = complex(0)
            return 0
        else:
            self.zero = complex(0)
            self.one = complex(1)
            return 1

    def __repr__(self):
        return str(self.zero) + " |0> + " + str(self.one) + " |1>\n"


qb = Qubit(1, 0)
print(qb)
qb.hgate()
print(qb)
qb.hgate()
print(qb)
