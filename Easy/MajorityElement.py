class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashset = set(nums) # remove duplicates
        for i in hashset: # loop through the set
            if nums.count(i) > len(nums)/2: # if the count of the element is greater than half the length of the list
                return i # return the element
            else: # if not continue the loop
                continue
        return None # if no element is found, return None

