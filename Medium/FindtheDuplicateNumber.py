class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()  # Sort the list
        for i in range(len(nums) - 1):  # Loop through the list and check if the next number is the same
            if nums[i] == nums[i + 1]:  # If it is, return the number
                return nums[i]  # Return the number
