class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        #create a matrix [names[i], height[i]], ordenate the array according to height

        def sortSecond(val):
            return val[1]

        n = len(names)
        info = [None]*n
        ordered = [None]*n

        for i in range (n):
            info[i] = [names[i], heights[i]]

        info.sort(key=sortSecond,reverse=True)

        for j in range (n):
            ordered[j] = info[j][0]
        return ordered
        
        