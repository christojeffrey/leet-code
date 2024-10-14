class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split(' ')
        words.reverse()
        
        ans = ''
        for i in range(len(words)):

            if(words[i] != ''):
                ans += words[i]
                if(i != len(words) - 1):
                    ans += ' '

        return ans