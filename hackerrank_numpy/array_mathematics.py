import numpy as np

n, m = map(int, input().split())
# print(n, m)

arrA = np.array([input().split() for _ in range(n)], int)
arrB = np.array([input().split() for _ in range(n)], int)

'''
Above line 6 and 7 can be replaced by below short hand as well 
arrA, arrB = (np.array([input().split() for _ in range(n)], int) for _ in range(2))
'''
print(arrA + arrB, arrA - arrB, arrA * arrB, arrA // arrB, arrA % arrB, arrA ** arrB, sep='\n')
