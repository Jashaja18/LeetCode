class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = [[]]

        for i in candidates:
            for j in target:
