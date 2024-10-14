class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = -1
        right = len(s)


        invalid = True
        while(invalid):
            left += 1
            if(right < left or left >= len(s)):
                break
            if(s[left].isalnum()):
                invalid = False
        
        invalid = True
        while(invalid):
            right -= 1
            if(right < left or right <= 0):
                break
            if(s[right].isalnum()):
                invalid = False

        while(left <= right):

            leftChar = s[left].lower()
            rightChar = s[right].lower()

            if(leftChar != rightChar):
                return False


            invalid = True
            while(invalid):
                left += 1
                if(right < left):
                    break
                if(s[left].isalnum()):
                    invalid = False
            invalid = True
            while(invalid):
                right -= 1
                if(right < left):
                    break
                if(s[right].isalnum()):
                    invalid = False
        
        return True

        