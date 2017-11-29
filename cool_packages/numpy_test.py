import numpy

n = numpy.arange(27)
print(n)

n.reshape(3, 3, 3)
print(n.view())
