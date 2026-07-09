class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # (self, nums, val)
        # returns 
        # in-place: reusing original memory addresses
        # typically in sorting algorithms
        #  modifies the input data structure directly 
        # instead of creating a completely new copy
        # remove elements==val from nums
        # return the length of nums after removals
        # if val, move element all the way to end of nums (nums[length-1])
        
        i = 0  # write pointer
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
                