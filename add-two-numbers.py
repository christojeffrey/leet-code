from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:


        remainder = 0


        next1 = l1
        next2 = l2
        firstNode = ListNode()
        prevNode = firstNode

        while(next1 != None or next2 != None):

            next1val = 0
            if(next1 != None):
                next1val = next1.val
            
            next2val = 0
            if(next2 != None):
                next2val = next2.val

            total = next1val + next2val + remainder

            ans = total % 10
            # print(ans)

            if total >= 10:
                remainder = 1
            else:
                remainder = 0

            newNode = ListNode()
            newNode.val = ans 
            prevNode.next = newNode

            prevNode = newNode

            if(next1 != None):
                next1 = next1.next
            if(next2 != None):
                next2 = next2.next
            


            

        if(remainder == 1):
            newNode = ListNode()
            newNode.val = 1
            prevNode.next = newNode
        
        return firstNode.next
    


sol = Solution()

