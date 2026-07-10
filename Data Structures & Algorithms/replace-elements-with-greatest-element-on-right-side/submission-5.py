class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # One Pass Iteration: traverse right-left
        # to calculate max
        # Initialize max_so_far as -1 (for the last element)
        ans = [0] * len(arr)
        rightMax = -1
        for i in range(len(arr) - 1, -1, -1): #stops at 0
            ans[i] = rightMax
            rightMax = max(arr[i], rightMax)
        return ans