class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hashing maybe: same hashcode
        #return immediately after finding a duplicate
        # head (i) and tail (j) pointers (too slow)
        # data structure (sets dont allow duplicates)
        # It'd be nice if you can sort then so you
        # can easily look at neighbors!
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False


