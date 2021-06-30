def staircase(n):
    for i in range(1, n + 1):
        print((" ") * (n - i) + ("#" * i))


def staircase_diffapp(n):
    for i in range(1, n + 1):
        print(str('#' * i).rjust(n))


staircase(5)
staircase_diffapp(6)
