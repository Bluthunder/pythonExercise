import os


#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compare_triplets(a, b):
    a_score, b_score = 0, 0
    for i in range(len(a)):
        if a[i] > b[i]:
            a_score += 1
        elif b[i] > a[i]:
            b_score += 1
    return [a_score, b_score]


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    alice = list(map(int, input().rstrip().split()))

    bob = list(map(int, input().rstrip().split()))

    result = compare_triplets(alice, bob)

   # fptr.write(' '.join(map(str, result)))
   # fptr.write('\n')

   # fptr.close()
