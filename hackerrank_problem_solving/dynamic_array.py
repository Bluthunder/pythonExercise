def dynamicArray(n, queries):
    seq = [[] for _ in range(n)]
    lastAns = 0
    res = []

    for q in queries:
        index = (q[1] ^ lastAns) % n
        if q[0] == 1:
            seq[index].append(q[2])
        else:
            pos = q[2] % len(seq[index])
            lastAns = seq[index][pos]
            res.append(lastAns)

    return res

if __name__ == '__main__':

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

   # fptr.close()


