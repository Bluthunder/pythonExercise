def jumpingOnClouds(c):
    # count = 0
    # p = []
    # for i in range(len(c)):
    #     if c[i] == 0:
    #         count = count + 1
    #         p.append(i)
    # return p
    i = 0
    jumps = 0
    if len(c) == 1:
        return 0
    while i < len(c):
        if i + 2 < len(c) and c[i + 2] == 0:
            jumps += 1
            i += 2
        elif i + 1 < len(c) and c[i + 1] == 0:
            jumps += 1
            i += 1
        else:
            i += 1
    return jumps


if __name__ == '__main__':
    n = int(input().strip())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    print(result)
