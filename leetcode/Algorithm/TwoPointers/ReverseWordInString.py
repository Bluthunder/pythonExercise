def reverseWordsInString(s):
    words = s.split()
    reversedWords = []
    for i in range(0, len(words)):
        word = words[i]
        nW = words[::-1]
        reversedWords.append(nW)
    return " ".join(reversedWords)


if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    print(reverseWordsInString(s))
