"""
Date - 20.06.2024
DSA - Binary Search tree

Here we would be discussing and solving problems based in binary search tree.
Questions are based on mostly from Data Structures and Algorithmic Thinking with Python

"""


class BSTNode:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def FindMax(self, root):
        pass


class Solution:
    def is_bst(self, root):
        if root is None:
            return 1

        # check if the left subtree exists and max value of node in left subtree
        # is greater than root then return 0
        if root.left is not None and FindMax(root.left) > root.data:
            return 0

        # check if the right subtree exists and min value of node in right subtree
        # is lesser than root then return 0
        if root.right is not None and FinMin(root.right) < root.data:
            return 0

        # false if recursively, the left and right is not BST
        if not self.is_bst(root.left) or not self.is_bst(root.right):
            return 0

        # true if all other conditions are false.
        return 1
