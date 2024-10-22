from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sums = []
        def addToSum(root: TreeNode, depth):
            if(len(sums) < depth + 1):
                sums.append(0)
            sums[depth] += root.val
            if(root.left):
                addToSum(root.left, depth+1)
            if(root.right):
                addToSum(root.right, depth+1)
        
        if(root):
            addToSum(root, 0)
        
        if(len(sums) < k):
            return -1
        sums.sort(reverse=True)
        return sums[k-1]

        