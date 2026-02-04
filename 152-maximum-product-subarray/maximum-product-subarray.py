class Solution(object):
    def maxProduct(self, nums):
        # code here
        n=len(nums)
        currmin=nums[0]
        currmax=nums[0]
        maxprod=nums[0]
        
        for i in range(1,n):
            
            temp=max(nums[i],currmin*nums[i],currmax*nums[i])
            
            currmin=min(nums[i],currmin*nums[i],currmax*nums[i])
            
            currmax=temp
            
            maxprod=max(maxprod,currmax)
            
        return maxprod
            
        