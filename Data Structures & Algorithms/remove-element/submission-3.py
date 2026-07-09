class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # (self, nums, val)
        # returns k (count elements != val as you go)
        # in-place: reusing original memory addresses
        # two pointers: compare and swap
        # sorting

        # go through the array
        # when you encounter a number == to the value
        # you want to delete, have k-pointer stay there 
        # until you have a number != val (i pointer)
        # you can then make the k pointer == i pointer (swapping)
        # and increment k (repeat prev steps)

        k = 0
        for i in range(len(nums)):
            if nums[i] != val: #increment k
                e = nums[k]
                nums[k] = nums[i] # swap elements != val to front
                nums[i] = e
                k += 1 # track e != val
        return k
                