# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        print("preorder", preorder)
        print("inorder", inorder)
        if (len(preorder) == 0):
            return TreeNode()

        
        center = preorder[0]

        centerLocation = 0
        for index in range(len(inorder)):
            if(inorder[index] == center):
                centerLocation = index
                break

        leftInorder = inorder[:centerLocation]
        rightInorder = inorder[centerLocation + 1:]
        print(center, leftInorder, rightInorder)




        leftNode = None
        if(len(leftInorder) >= 1): # it has left
            leftPreorder = preorder[1:len(leftInorder) + 1]

            leftNode = self.buildTree(leftPreorder, leftInorder)
        
        rightNode = None
        if(len(rightInorder) >= 1): # it has right
            rightPreorder = preorder[len(leftInorder) + 1:]
            rightNode = self.buildTree(rightPreorder, rightInorder)

        newNode = TreeNode()
        newNode.val = center
        newNode.left = leftNode
        newNode.right = rightNode

        return newNode

        
        