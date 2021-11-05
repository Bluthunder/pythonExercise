from collections import Counter


def checkMagazine(magazine, note):
    c1 = Counter(magazine)
    c2 = Counter(note)
    flag = True
    for k, v in c2.items():
        if k in c1 and c1[k] >= v:
            continue
        else:
            flag = False
            break

    if flag:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    m = int(first_multiple_input[0])
    n = int(first_multiple_input[1])
    magazine = input().rstrip().split()
    note = input().rstrip().split()
    checkMagazine(magazine, note)

