def commonChild(s1, s2):
    dp = [[0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
    for i in range(len(s1) - 1, -1, -1):
        for j in range(len(s2) - 1, -1, -1):
            if s1[i] == s2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

    return dp[0][0]


if __name__ == '__main__':
    s1 = input()
    s2 = input()
    result = commonChild(s1, s2)
