class Solution:
    def reverse(self, x: int) -> int:
        if x<-2**(31) or x>2**(31)+1:
            return 0
        neg=0
        if x<0:
            neg=1
            x=x*(-1)
        s=0
        l=str(x)
        l=l[::-1]
        s=int(l)
        if s<-2**(31) or s>2**(31)+1:
            return 0
        if neg==1:
            return -s
        return s