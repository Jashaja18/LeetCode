class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        hashset = set()
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    if arr[i] + arr[j] + arr[k] == target:
                        hashset.add((arr[i], arr[j], arr[k]))
        return len(hashset)
