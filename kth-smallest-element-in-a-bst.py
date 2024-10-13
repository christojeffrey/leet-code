from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.makeInorder(root)[k-1]
    
    def makeInorder(self, root: Optional[TreeNode]) -> List[int]:
        if(root == None):
            return []
        return self.makeInorder(root.left) + [root.val] + self.makeInorder(root.right)