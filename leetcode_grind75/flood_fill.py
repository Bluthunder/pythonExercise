# from typing import List
#
#
# class Solution:
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
#         start = image[sr][sc]
#
#         def dfs(image, sr, sc, color, starting):
#             if sr < 0 or sr > len(image) - 1 or sc < 0 or sc > len(image[0]) - 1 or image[sr][sc] == color or image[sr][
#                 sc] != starting:
#                 return
#             image[sr][sc] = color
#             dfs(image, sr + 1, sc, color, starting)
#             dfs(image, sr - 1, sc, color, starting)
#             dfs(image, sr, sc + 1, color, starting)
#             dfs(image, sr, sc - 1, color, starting)
#
#         dfs(image, sr, sc, color, start)
#         return image
#
#


def flood_fill(image, sr, sc, color):
    start_color = image[sr][sc]

    def backtrack(image, sr, sc, color, start):
        row, col = len(image), len(image[0])

        if sr < 0 or sr >= row or sc < 0 or sc >= col or image[sr][sc] == start_color or image[sr][sc] != start_color:
            return

        image[sr][sc] = start_color

        backtrack(image, sr + 1, sc, color, start_color)
        backtrack(image, sr - 1, sc, color, start_color)
        backtrack(image, sr, sc + 1, color, start_color)
        backtrack(image, sr, sc - 1, color, start_color)

    backtrack(image, sr, sc, color, start_color)
    return image


if __name__ == '__main__':
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr, sc, color = 1, 1, 2
    print(flood_fill(image, sr, sc, color))
