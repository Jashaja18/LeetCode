class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0  # Set the start to 0
        end = x  # Set the end to the number
        while start <= end:  # While the start is less than or equal to the end
            mid = (start + end) // 2  # Set the middle to the start plus the end divided by 2
            if mid * mid == x:  # If the middle times the middle is equal to the number
                return mid  # Return the middle
            elif mid * mid < x:  # If the middle times the middle is less than the number
                start = mid + 1  # Set the start to the middle plus 1
            else:  # If the middle times the middle is greater than the number
                end = mid - 1  # Set the end to the middle minus 1
