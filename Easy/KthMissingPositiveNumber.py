class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        start = 0  # start of the array
        end = len(arr) - 1  # end of the array
        while start <= end:  # while start is less than or equal to end
            mid = (start + end) // 2  # find the middle of the array
            if arr[mid] - mid - 1 < k:
                start = mid + 1  # set start to the middle plus 1
            else:
                end = mid - 1  # set end to the middle minus 1
        return start + k  # return start plus k
