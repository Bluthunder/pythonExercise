import numpy


def arrays(arr):
    # complete this function
    # use numpy.array
    rev_arr = arr[::-1]
    return numpy.array(rev_arr, float)


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
