class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        n=x
        temp=0
        while x>0:
            temp*=10
            temp+=x%10
            x=x//10
        if temp==n:
            return True
        else:
            return False