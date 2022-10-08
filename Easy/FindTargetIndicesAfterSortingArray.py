class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums) # sorted() returns a new list
        target_indices = [] # list to store target indices
        for i in range(len(nums)): # iterate through nums list to find target indices
            if sorted_nums[i] == target:
                target_indices.append(i) # append target index to target_indices list
        return target_indices # return target_indices list