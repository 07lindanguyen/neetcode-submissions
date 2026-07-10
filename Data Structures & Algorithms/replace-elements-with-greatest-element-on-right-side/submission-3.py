class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # giving selection sort (find max of unsorted area)
        # recursion?
        result = []
        for i in range(len(arr)-1):
            arr[i] = 0
            result.append(max(arr))
        result.append(-1)
        return result