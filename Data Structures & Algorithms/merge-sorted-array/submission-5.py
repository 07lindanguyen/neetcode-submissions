class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        for i in range(m, m + n):
            nums1[i] = nums2[i - m]
        nums1.sort()
        """ # Double pointer that compares numbers in N and M section
        last = m + n - 1 # tracks where to place the next largest element in nums1
        i = m - 1   # index of last element in nums1 (before zeros)
        j = n - 1   # index of last element in nums2

        # Keep placing the largest element from the two arrays into the end of nums1
        while j >= 0:   # we only need to process all elements of nums2
        # Are there still valid elements left in nums1? And compares
            if i >= 0 and nums1[i] > nums2[j]:
                # The largest remaining element is in nums1
                nums1[last] = nums1[i]
                i -= 1   # move pointer in nums1 leftwards
            else: # when i has no remaining elements/j>i, fill in with j's
                nums1[last] = nums2[j]
                j -= 1   # move pointer in nums2 leftwards
            last -= 1    # move the 'last' pointer leftwards
                    