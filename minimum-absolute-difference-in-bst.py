from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def getSmallestValue(self, root: TreeNode) -> int:    
        if(root.left):
            return self.getSmallestValue(root.left)
        
        return root.val
    
    def getBiggestValue(self, root: TreeNode) -> int:
        if(root.right):
            return self.getBiggestValue(root.right)
        
        return root.val

            
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if(root == None):
            return None # huh?
        

        minimumDiff = None
        if(root.left):
            biggestLeft = self.getBiggestValue(root.left)
            minimumDiff = root.val - biggestLeft

            minimumLeft = self.getMinimumDifference(root.left)

            if(minimumLeft != None and minimumLeft < minimumDiff):
                minimumDiff = minimumLeft


        if(root.right):
            smallestRight = self.getSmallestValue(root.right)
            
            if(minimumDiff == None or smallestRight - root.val < minimumDiff):
                minimumDiff = smallestRight - root.val


            minimumRight = self.getMinimumDifference(root.right)

            if(minimumRight != None and minimumRight < minimumDiff):
                minimumDiff = minimumRight
            
        return minimumDiff