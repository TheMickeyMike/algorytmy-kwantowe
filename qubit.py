from numpy import matrix
from numpy import linalg
import numpy
import math
import random


class Qubit:
    def __init__(self, a, b):
        self.zero = complex(a)
        self.one = complex(b)

    def xgate(self):
        '''Apply a NOT (X) gate'''
        self.zero, self.one = self.one, self.zero
        return self

    def hgate(self):
        '''Apply a Hadamard gate'''
        h = matrix([[1, 1], [1, -1]]) * (1.0 / math.sqrt(2))
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
