from collections import Counter

def isValid(s):
    d = Counter(s)
   # print(d.values())
   # print(len(set(d.values())))

    # case 1 : Same frequencies of chars in string
    if len(set(d.values())) == 1:
        return "YES"

    # case 2 : More than 2 Unique Frequencies
    elif len(set(d.values())) > 2:
        return "NO"

    # case 3 : 2 Unique Frequencies
    else:
        for key in d:
            d[key] -= 1
            temp = list(d.values())

            # Remove Zero
            try:
                temp.remove(0)
            except:
                pass
            if len(set(temp)) == 1:
                return "YES"
            else:
                d[key] += 1
    return "NO"


if __name__ == '__main__':
    s = input()
    result = isValid(s)
    print(result)