import math
class Solution:
    def intToRoman(self, num: int) -> str:
        res = ''
        currentNumber = num
        while(currentNumber != 0):
            # check the length of current number

            length = 0
            
            copy = currentNumber
            

            while(copy >= 10):
                copy = math.floor(copy / 10) 
                length += 1
            
            tens = 1
            for i in range(length):
                tens *= 10
            
            focusNumber = math.floor(currentNumber / tens)
            
            
            # print(length, focusNumber)
            # append to res according to length, and focusNumber

            if(length >= 3): # 1000+
                # add M 'focusNumber' time
                for _ in range(focusNumber):
                    res += 'M'
                currentNumber = currentNumber % tens
            elif(length == 2): # 100+
                if(focusNumber == 9):
                    res += 'CM'
                    currentNumber = currentNumber % tens
                elif(focusNumber == 4):
                    res += 'CD'
                    currentNumber = currentNumber % tens
                elif(focusNumber >= 5):
                    res += 'D'
                    currentNumber -= 500
                else:
                    for _ in range(focusNumber):
                        res += 'C'
                    currentNumber = currentNumber % tens

            elif(length == 1): # 10+
                if(focusNumber == 9):
                    res += 'XC'
                    currentNumber = currentNumber % tens
                elif(focusNumber == 4):
                    res += 'XL'
                    currentNumber = currentNumber % tens
                elif(focusNumber >= 5):
                    res += 'L'
                    currentNumber -= 50
                else:
                    for _ in range(focusNumber):
                        res += 'X'
                    currentNumber = currentNumber % tens
            else: # 0 - 9
                if(focusNumber == 9):
                    res += 'IX'
                    currentNumber = currentNumber % tens
                elif(focusNumber == 4):
                    res += 'IV'
                    currentNumber = currentNumber % tens
                elif(focusNumber >= 5):
                    res += 'V'
                    currentNumber -= 5
                else:
                    for _ in range(focusNumber):
                        res += 'I'
                    currentNumber = currentNumber % tens
        return res



sol = Solution()

res = sol.intToRoman(10)
print(res)
