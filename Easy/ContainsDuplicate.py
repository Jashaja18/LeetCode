def containsDuplicate(self, nums: List[int]) -> bool:
    hashset = set(nums)
    for num in nums: