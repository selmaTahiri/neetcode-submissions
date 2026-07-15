class Solution:
    def isAnagram(self, s, t):
        a=sorted(s)
        b=sorted(t)
        if a==b:
            return True
        return False
        
        
test=Solution()
print(test.isAnagram("racecar", "carrace"))
print(test.isAnagram("jar", "jam"))