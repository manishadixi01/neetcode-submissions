class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        final = 0
        total = 0
        total = sum(arr[:k])
        if total//k >= threshold:
            final += 1

        for j in range(k, len(arr)):
            total += arr[j] - arr[j-k]
            if total//k >= threshold:
                final += 1
        return final


        