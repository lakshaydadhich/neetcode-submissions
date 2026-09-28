class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        a=[]
        for i in nums:
            if i!=0:
                a.append(i)

        for i in range(len(nums)):
            if i<len(a):
                nums[i]=a[i]
            else:
                nums[i]=0

      