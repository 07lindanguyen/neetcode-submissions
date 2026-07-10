class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # One Pass Iteration: traverse right-left
        # to calculate max 
        # Initialize max_so_far as -1 (for the last element)
        max_so_far = -1
        
        # Iterate over the array from right to left
        for i in range(len(arr) - 1, -1, -1):
            # Store the current element
            temp = arr[i]
            # Update the current element with max_so_far
            arr[i] = max_so_far
            # Update max_so_far if the current element is greater
            max_so_far = max(max_so_far, temp)
        
        return arr