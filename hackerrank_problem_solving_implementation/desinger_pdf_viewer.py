from collections import Counter


def designerPdfViewer(h, word):
    maxHeight = 0
    for i in range(len(word)):
        if (h[ord(word[i]) - 97] > maxHeight):
            maxHeight = h[ord(word[i]) - 97]
    return (len(word) * 1 * maxHeight)

# def designerPdfViewer(h,word):
#     size = [int(i) for i in input().split()]
#     word = [size[ord(c) - ord('a')] for c in input()]
#     print(max(word) * len(word))

if __name__ == '__main__':
    h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    word = 'abc'
    designerPdfViewer(h, word)
