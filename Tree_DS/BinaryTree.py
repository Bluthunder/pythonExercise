"""
Date - 20.05.2024
DSA - Tree

This is the simplest representation of a tree in python
"""


class BinaryTreeNode:

    def __init__(self, data, children= []):
        self.data = data
        self.children = children

    def __str__(self, level=0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def addchildnode(self, BinaryTreeNode):
        self.children.append(BinaryTreeNode)


if __name__ == '__main__':
    TreeNode = BinaryTreeNode('Books', [])
    cse = BinaryTreeNode('CSE', [])
    ee = BinaryTreeNode('EE', [])
    TreeNode.addchildnode(cse)
    TreeNode.addchildnode(ee)

    dsa = BinaryTreeNode('DSA', [])
    os = BinaryTreeNode('OS', [])
    cse.addchildnode(dsa)
    cse.addchildnode(os)

    powersystem = BinaryTreeNode('POWER SYSTEM', [])
    machines = BinaryTreeNode('MACHINES', [])
    ee.addchildnode(powersystem)
    ee.addchildnode(machines)

    print(TreeNode)
