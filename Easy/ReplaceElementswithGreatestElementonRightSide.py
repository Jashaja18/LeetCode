class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        hashset = set(arr)

        for i in range(len(arr)):
