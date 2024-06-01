#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    maxi = max(arr)
    mini = min(arr)

    max_sum = sum(arr) - mini

    mini_sum = sum(arr) - maxi

    print(f'{mini_sum} {max_sum}')




if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    miniMaxSum(arr)
