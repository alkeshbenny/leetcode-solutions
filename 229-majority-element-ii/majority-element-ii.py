class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)
        freq={}
        res=[]
        
        for ele in nums:
            freq[ele]=freq.get(ele,0)+1
            
        for ele,cnt in freq.items():
            if cnt>n//3:
                res.append(ele)
                
        if len(res)== 2 and res[0]>res[1]:
            res[0],res[1]=res[1],res[0]
            
    
        return res