class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # nums has a length of n
        # double the array the array elements
        """ TOO SLOW
        double_length = len(nums)*2
        ans = [0] * double_length
        for i in range(len(nums)):
            ans[i] = nums[i]
        for j in range(len(nums)):
            ans[j+len(nums)] = nums[j]
        return ans
        """
        """ SHORTCUT
        doubled = nums * 2
        return doubled
        """
        
        ans = []
        for i in range(2): ## loop twice
            for i in nums: ## iterate and append
                ans.append(i)
        return ans

        """ USING LOOPS 
        ans = []
        for i in range(2): ## loop twice
            for i in nums: ## iterate and append
                ans.append(i)
        return ans
        """
