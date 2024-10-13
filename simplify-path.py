class Solution:
    def simplifyPath(self, path: str) -> str:

        dirs = []
        potentialDirs = path.split('/')
        for potentialDir in potentialDirs:
            if(potentialDir == ''):
                continue
            elif(potentialDir == '.'):
                continue
            elif(potentialDir == '..'):
                dirs = dirs [:len(dirs) - 1]
            else:
                dirs.append(potentialDir)
        
        ans = ''
        for dir in dirs:
            ans += "/" + dir

        if ans == '':
            ans = "/"
        return ans

sol = Solution()
ans = sol.simplifyPath("/home/user/Documents/../Pictures")
print(ans)
