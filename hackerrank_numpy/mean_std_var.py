import numpy

N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)], int)
print(numpy.mean(A, axis=1), numpy.var(A, axis=0), round(numpy.std(A), 11), sep='\n')