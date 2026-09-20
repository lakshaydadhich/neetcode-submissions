class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left_product=[1]*n
        right_product=[1]*n

        left=1
        for i in range(n):
            left_product[i]=left
            left=left*nums[i]

        right=1
        for i in range(n-1,-1,-1):
            right_product[i]=right
            right=right*nums[i]

        answer=[]
        for i in range(n):
            answer.append(left_product[i]*right_product[i])
        return answer