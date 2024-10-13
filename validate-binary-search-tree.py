# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:


    def isAnyBiggerThan(self, root: TreeNode, target: int) -> int:

        if(root.val >= target):
            return True
        
        if(root.left != None and root.right == None):
            return self.isAnyBiggerThan(root.left, target)
        
        if(root.left == None and root.right != None):
            return self.isAnyBiggerThan(root.right, target)
        
        if(root.left != None and root.right != None):
            return self.isAnyBiggerThan(root.left, target) or self.isAnyBiggerThan(root.right, target)
        
        return False

    def isAnySmallerThan(self, root: TreeNode, target: int) -> int:

        if(root.val <= target):
            return True
        
        if(root.left != None and root.right == None):
            return self.isAnySmallerThan(root.left, target)
        
        if(root.left == None and root.right != None):
            return self.isAnySmallerThan(root.right, target)
        
        if(root.left != None and root.right != None):
            return self.isAnySmallerThan(root.left, target) or self.isAnySmallerThan(root.right, target)
        
        return False


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if(root == None):
            return True


        if(root.left):
            isLeftInvalid = self.isAnyBiggerThan(root.left, root.val) or not self.isValidBST(root.left)
            if(isLeftInvalid):
                return False
        
        if(root.right):
            isRightInvalid = self.isAnySmallerThan(root.right, root.val) or not self.isValidBST(root.right)
            if(isRightInvalid):
                return False     
            
        return True