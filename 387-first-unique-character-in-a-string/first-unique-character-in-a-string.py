class Solution(object):
    def firstUniqChar(self, s):
        #code here
        freq={}
        
        for c in s:
            freq[c]=freq.get(c,0)+1
            
        for c in s:
            if freq[c] ==1:
                return s.index(c)
                
        
        return -1
        
    
        