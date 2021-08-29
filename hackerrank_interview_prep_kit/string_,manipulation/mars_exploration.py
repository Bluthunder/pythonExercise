def marsExploration(s):
    exp = len(s)*"SOS"
    count = 0
    for i in range(len(s)):
        if exp[i] != s[i]:
            count += 1
    return count

if __name__ == '__main__':
    s = input()
    result = marsExploration(s)