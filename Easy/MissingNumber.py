class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()  # Sort the list
        for i in range(len(nums)):  # Loop through the list and check if the index is equal to the value
            if i != nums[i]:  # If not, return the index
                return i
        return len(nums)  # if the last number is missing return the length of the list
