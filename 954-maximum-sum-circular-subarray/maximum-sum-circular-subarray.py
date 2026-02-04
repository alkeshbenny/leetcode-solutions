class Solution(object):
    def maxSubarraySumCircular(self, nums):
        # code here
        currmax=nums[0]
        currmin=nums[0]
        totalsum=0
        maxsum=nums[0]
        minsum=nums[0]
        
        for i in range(1,len(nums)):
            currmax=max(currmax+nums[i],nums[i])
            maxsum=max(maxsum,currmax)
            
            currmin=min(currmin+nums[i],nums[i])
            minsum=min(minsum,currmin)
            
            totalsum=totalsum+nums[i]
        
        totalsum=totalsum+nums[0]
            
        normalsum=maxsum
        circularsum=totalsum-minsum
        
        if minsum==totalsum:
            return normalsum
            
        return max(normalsum,circularsum)
        
        
        