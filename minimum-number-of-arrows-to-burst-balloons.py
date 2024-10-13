from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # sort by right location of baloon, smallest to bigest
        # then 'shoot' that smallest baloon

        points.sort(key=lambda x: x[1])


        shootCount = 0
        while(len(points) != 0):
            shootLocation = points[0][1] 
            points = list(filter(lambda x: x[0] > shootLocation or x[1] < shootLocation, points))
            shootCount += 1
            
        return shootCount

    def OldfindMinArrowShots(self, points: List[List[int]]) -> int:
        locationToShoot = []

        for point in points:

            # check if any overlap
            overlapWithExisting = False
            for index in range(len(locationToShoot)):
                shootLocation = locationToShoot[index]


                # check if overlap
                if((point[0] >= shootLocation[0] and point[0] <= shootLocation[1]) or (shootLocation[0] >= point[0] and shootLocation[0] <= point[1])):
                    newOverlap = [max(point[0], shootLocation[0]), min(point[1], shootLocation[1])]

                    # update location to shoot
                    locationToShoot[index] = newOverlap
                    overlapWithExisting = True
                    break
                

            
            if(not overlapWithExisting):
                # add new
                locationToShoot.append(point)

        print(locationToShoot)
        return len(locationToShoot)


sol = Solution()
ans = sol.findMinArrowShots([[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]])
print(ans)