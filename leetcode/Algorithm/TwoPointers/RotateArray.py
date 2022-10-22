# Rotate array using new array , extra space.
def rotate(nums, k):
    newNum = []
    for i in range(0, len(nums)):
        j = (i + k) % (len(nums))  # ths would give new index for shifted numbers
        newNum.insert(j, nums[i])
    return newNum


# In place array rotation without extra space
def rotate1(numList, a):
    a = a % len(numList)
    n = len(numList) - a
    numList[:] = numList[n:] + numList[:n]
    return numList


if __name__ == "__main__":
    Nums = [1, 2, 3, 4, 5, 6, 7]
    K = 3
    print(rotate1(Nums, K))
