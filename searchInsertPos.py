class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
       #target < nums[0]
       #target > nums[-1]
       #target == nums[i]
       #target > nums[i] and target < nums[i+1]

        if target <= nums[0]:
            return 0
        elif target > nums[-1]:
            a = len(nums)
            return a
        elif target == nums[-1]:
            c = len(nums)-1
            return c
        

        for i in range (len(nums)-1):
            if target == nums[i]:
                return i
            if target > nums[i] and target < nums[i+1]:
                b = i+1
                return b


                    

        

        return 0
        