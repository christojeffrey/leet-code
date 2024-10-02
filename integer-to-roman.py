import math
class Solution:
    def intToRoman(self, num: int) -> str:
        res = ''
        currentNumber = num
        while(currentNumber != 0):
            # check the length of current number

            length = 0
            
            copy = currentNumber
            

            while(copy >  10):
                copy = math.floor(copy / 10) 
                length += 1
            
            print(length)
            tens = 1
            for i in range(length):
                tens *= 10
            
            focusNumber = math.floor(currentNumber / tens)
            
            
            # print(length, focusNumber)
            # append to res according to length, and focusNumber

            if(length >= 3): # 1000+
                # add M 'focusNumber' time
                for i in range(length):
                    res += 'M'
                currentNumber = currentNumber % tens
            elif(length == 2): # 100+
                pass
            elif(length == 1): # 10+
                pass
            else: # 0 - 9
                pass


        
        return res



sol = Solution()

sol.intToRoman(3749)
