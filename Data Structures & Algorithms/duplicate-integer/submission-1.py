class Solution:
    def hasDuplicate(self,nums:List[int])->bool:
        a={}
        for i in range(len(nums)):
            if nums[i] in a:
                a[nums[i]]+=1
            else:
                a[nums[i]]=1

        for key,value in a.items():
            if value>1:
                return True
        return False 