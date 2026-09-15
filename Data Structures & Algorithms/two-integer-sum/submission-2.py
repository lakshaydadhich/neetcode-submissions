class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      a={}
      for i in range(len(nums)):
        compliment=target-nums[i]
        if compliment in a:
            return [a[compliment],i]
        a[nums[i]]=i