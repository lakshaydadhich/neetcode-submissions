class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      maxx=nums[0]
      current=nums[0]
      for i in range(1,len(nums)):
        current=max(nums[i],current+nums[i])
        maxx=max(current,maxx)

      return maxx