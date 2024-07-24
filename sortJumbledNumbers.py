class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        res = [None]*len(nums)
        temp = [None]*len(nums)
        for i in range (len(nums)):
            res[i]=0
            temp[i]=0
            x=0
            num = str(nums[i])
            for digit in num:
                y = str(temp[i])
                temp[i] = int(str(y)+digit)
                digit = int(digit)
                digit = mapping[digit]
                x = int(str(x)+str(digit))
                res[i] = (x, temp[i], i)

        #res is a list of tuples, which is immutable, so i can't atribute another value to an item

        asw = sorted(res, key=lambda x: (x[0], x[2]))
        #creates an anonymous function that takes x (which is a tuple, an element of res) and
        #returns a new tuple (x[0],x[2]), x[0] is the mapped value and x[2] is the original index position
        #the sorted function uses the lambda function to first compare the x[0] values and if they are the same,
        #it uses x[2] to maintain the relative orde

        result = [original for _, original, _ in asw]
        #unpacks the tuple into the 3 elements, tuple[0] and tuple[2] are ignored (_)

            
        return result
        
            
