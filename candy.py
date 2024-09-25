from typing import List
# checked discussion



class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [0] * len(ratings)
        


        candies[0] = 1



        previousRatings = ratings[0]
        # left to right: if current rating is bigger than left hand rating, my candy is left hand + 1
        for i in range (1, len(ratings)):
            currentRatings = ratings[i]
            previousRatings = ratings[i-1]
            if currentRatings > previousRatings :
                candies[i] = candies[i-1]+1
            else : 
                candies [i] = 1



        previousRatings = ratings[len(ratings) - 1]
        # right to left: ditto previous
        for i in range (len(ratings) - 2,-1,-1): # (1,5,1): 1,2,3,4
            currentRatings = ratings[i]
            previousRatings = ratings[i+1]
            if currentRatings > previousRatings :
                currentCandy = candies[i]
                previousCandy = candies[i+1]
                if currentCandy <= previousCandy :
                    candies[i] = previousCandy+1


        
        print(candies)

        


        return sum(candies)




sol = Solution()
ans  = sol.candy([1,2,3,2,1])
print("ans")
print(ans)
        