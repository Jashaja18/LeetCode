class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        result = []
        for i in range(len(nums)):
            for j in self.permute(nums[:i] + nums[i + 1:]):
                result.append([nums[i]] + j)
        return result