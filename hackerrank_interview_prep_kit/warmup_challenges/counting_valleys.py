def countingValleys(n, steps):
    valley = seaLevel = 0
    for step in steps:
        if step == "U":
            seaLevel += 1
        else:
            seaLevel -= 1
        if step == "U" and seaLevel == 0:
            valley += 1

    return valley


if __name__ == '__main__':
    steps = int(input().strip())
    path = input()
    result = countingValleys(steps, path)
    print(result)
