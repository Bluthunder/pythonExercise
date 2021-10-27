import os


def hackerrankInString(s):
    # Write your code here

    a = ['h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k']
    for i in s:
        if i == a[0]:
            a.pop(0)
        if len(a) == 0:
            return "YES"
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
