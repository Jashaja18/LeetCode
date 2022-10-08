class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for i in range(len(nums1)):
            for j in range(nums2.index(nums1[i]) + 1, len(nums2)):
                if nums2[j] > nums1[i]:
                    result.append(nums2[j])
                    break
            else:
                result.append(-1)
        return result
    #     hashset = set()
    #     for i in range(len(nums1)):
    #         for j in range(i + 1, len(nums2)):
    #             if nums2[j] > nums1[i]:
    #                 hashset.add((nums1[i], nums2[j]))
    #                 break
    #     return [x[1] for x in hashset]
    #