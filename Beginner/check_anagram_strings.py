def check_anagram(str1, str2):
    sorted1 = sorted(str1.lower())
    sorted2 = sorted(str2.lower())

    if len(sorted1) == len(sorted2):
        if sorted1 == sorted2:
            print(str1+" and "+str2+ " are anagram")
        else:
            print(str1 + " and " + str2 + " aren't anagram")
    else:
        print(str1 + " and " + str2 + " can't be anagram")


if __name__ == '__main__':
    in_str1 = input("Enter your first string :")
    in_str2 = input("Enter your second string :")
    print("let the fun begin!!! ")
    check_anagram(in_str1, in_str2)