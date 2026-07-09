class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # nums is a list like [1,1,0,1,1]
        # I'm assuming parameters are just (self,nums)
        # traverse through entire array
        # and check for the longest, unbroken sequence
        # of ones
        # maybe have a double pointer
        # 1) traverse; 2) sum consecutive 1s; 3) after 0, repeat (2)
        # 1? sum; 0? break
        # sum before restarting
        max_count = [0]    
        sum = 0        
        for i in range(len(nums)):
            if nums[i] == 1:
                sum += 1
                max_count.append(sum)
            else:
                sum = 0
        return max(max_count)
            