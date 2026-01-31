class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        expected_sum=int(n*(n+1)/2)
        current_missing_sum=sum(nums)
        return expected_sum-current_missing_sum
        