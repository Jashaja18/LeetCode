class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumA = sum(aliceSizes) # Sum of Alice's candy
        sumB = sum(bobSizes) # Sum of Bob's candy
        diff = (sumA - sumB) // 2 # Difference between the two sums
        for i in aliceSizes: # Loop through Alice's candy
            if i - diff in bobSizes: # If the difference is in Bob's candy
                return [i, i - diff] # Return the two candies
