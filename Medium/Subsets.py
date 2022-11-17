class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # result is set to a empty list of an empty list
        result = [[]]

        # for loop in nums
        for i in nums:  # for loop in nums is O(n)
            # result is set to a list of result and a list of result + i
            result += [j + [i] for j in result]  # increment of result of j + [i] for j in result
        return result  # return result
