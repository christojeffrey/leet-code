from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        splitted = []
        currentRow = []
        currentLength = 0
        for word in words:
            if(currentLength + len(word) + max(0, len(currentRow)) <= maxWidth):
                currentRow.append(word)
                currentLength += len(word)
            else:
                splitted.append(currentRow)
                currentRow = [word]
                currentLength = len(word)
        
        if(len(currentRow) != 0):
            splitted.append(currentRow)

        
        result = []
        for rowIndex in range(len(splitted)):
            row = splitted[rowIndex]
            spaceLeft = maxWidth - sum([len(word) for word in row])
            divider = len(row) - 1
            print(spaceLeft, divider)

            if(rowIndex == len(splitted) - 1):
                ans = ''
                for wordIndex in range(len(row)):
                    ans += row[wordIndex]

                    if(wordIndex == len(row) - 1):
                        ans += ' ' * spaceLeft
                    else:
                        ans += ' '
                        spaceLeft -= 1

            else:
                if(divider == 0):
                    ans = row[0] + ' ' * spaceLeft
                else:
                    ans = ''
                    spacing = ' ' * int(spaceLeft / divider)
                    for index in range(len(row)):
                        ans += row[index]
                        if(index != len(row) - 1):
                            ans += spacing
                        if(spaceLeft % divider != 0):
                            ans += ' ' 
                            spaceLeft -= 1   
                print(ans)
            result.append(ans)


        return result


sol = Solution()
ans = sol.fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20)
print(ans)