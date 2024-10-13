# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if(root == None):
            return []

        fromLeft = []
        if(root.left != None):
            fromLeft = self.rightSideView(root.left)
        
        fromRight = []
        if(root.right != None):
            fromRight = self.rightSideView(root.right)
        
        return [root.val] + fromRight + fromLeft[len(fromRight):]
        