import os


def pairs(k, arr):
    a = set(arr)
    b = [value + k for value in arr]
    return len(a.intersection(b))
   # return len(set(a) & set([item + k for item in set(a)]))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()