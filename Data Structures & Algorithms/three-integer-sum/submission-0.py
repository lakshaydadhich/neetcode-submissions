class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=set()
        for i in range(len(nums)):
            seen={}
            for j in range(i+1,len(nums)):
                third=-(nums[i]+nums[j])
                if third in seen:
                    triplet=tuple(sorted([nums[i],nums[j],third]))
                    result.add(triplet)
                seen[nums[j]]=True
        return [list(i) for i in result]