class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):  # Loop through nums2 (the second array)
            nums1[m + i] = nums2[i]  # Add nums2 to nums1 (the first array)
            for j in range(m + i, 0, -1):  # Loop through nums1 (the first array)
                if nums1[j] < nums1[j - 1]:  # If the current number is less than the previous number in nums1
                    nums1[j], nums1[j - 1] = nums1[j - 1], nums1[j]  # Swap the two numbers in nums1 (the first array)
                else:  # If the current number is greater than the previous number (or equal)
                    break
