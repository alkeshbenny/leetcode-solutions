class Solution(object):
    def trimmer(self,s):
        firstone=s.find('1')
        return s[firstone:] if firstone!=-1 else "0"
        
    def addBinary(self, a, b):
        
        s1=self.trimmer(a)
        s2=self.trimmer(b)
        
        n=len(a)
        m=len(b)
        
        if n < m:
            s1,s2=s2,s1
            n,m=m,n
            
        j=m-1
        carry=0
        result=[]
        
        for i in range(n-1,-1,-1):
            bit1=int(s1[i])
            bitsum=bit1+carry
            
            if j>=0:
                bit2=int(s2[j])
                bitsum+=bit2
                j-=1
                
            bit=bitsum%2
            carry=bitsum//2
            
            result.append(str(bit))
        
        if carry>0:
            result.append('1')
            
        return ''.join(result[::-1])
            
        