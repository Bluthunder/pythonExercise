#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    for val in a:
        if a.count(val) == 1:
            result = val
            return result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # n = int(input().strip())
    #
    # a = list(map(int, input().rstrip().split()))

    a = [1, 2, 3, 4, 3, 2, 1]

    result = lonelyinteger(a)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
