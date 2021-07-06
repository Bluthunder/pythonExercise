def breakingRecords(scores):
    high_score, low_score, low_score_nos, high_score_nos = scores[0], scores[0], 0, 0
    for score in scores:
        if score > high_score:
            high_score, high_score_nos = score, high_score_nos + 1
        elif score < low_score:
            low_score, low_score_nos = score, low_score_nos + 1
    print(high_score_nos, low_score_nos)


if __name__ == '__main__':
    n = int(input())
    score = list(map(int, input().split()))
    breakingRecords(score)
