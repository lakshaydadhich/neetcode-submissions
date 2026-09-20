class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum=0
        for i in range(len(nums)):
            sum=sum+nums[i]

        n=len(nums)
        total=n*(n+1)//2

        missing=total-sum
        return missing
        