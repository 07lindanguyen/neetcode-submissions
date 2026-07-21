class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        PointMap = {}
        
        for point in points:
            # origin is (0, 0), so directly use the coordinates
            distance = (point[0]**2 + point[1]**2)**0.5
            PointMap[tuple(point)] = distance
        
        invertDict = {}
        for key, value in PointMap.items():
            if value not in invertDict:
                invertDict[value] = [list(key)]
            else: 
                # same distance? append to the list of lists
                # that record all points with same distance
                invertDict[value].append(list(key))
        
        Result = []
        for a in range(k):
            MinDist = min(invertDict)
            # get point with min dist
            closestPoints = invertDict.get(MinDist)
            Result.append(closestPoints.pop(0))
            # If there are no more points in closestPoints
            # or list is empty, remove it from dictionary
            if not closestPoints:
                invertDict.pop(MinDist)

        return Result            
                       