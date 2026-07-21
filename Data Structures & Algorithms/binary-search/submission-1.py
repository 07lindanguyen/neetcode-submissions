class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        
        # Empty of negative
        while L <= R:
            mid = L + (R - L) // 2
            # change the start (R) or end (L) of array
            # Middle exclusive
            if target > nums[mid]:
                L = mid + 1
            elif target < nums[mid]:
                R = mid - 1
            else:
                return mid
        return -1
