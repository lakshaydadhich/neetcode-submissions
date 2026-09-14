class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      dictt={}
      for i in range(len(nums)):
        compliment=target-nums[i]
        if compliment in dictt:
            return [dictt[compliment],i]
        dictt[nums[i]]=i