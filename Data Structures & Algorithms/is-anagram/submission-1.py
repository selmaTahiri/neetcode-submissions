class Solution:
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        dico1={}
        for lettre in s:
            if lettre not in dico1:
                dico1[lettre]=1
            else:
                dico1[lettre]+=1
        dico2={}
        for lettre in t:
            if lettre not in dico2:
                dico2[lettre]=1
            else:
                dico2[lettre]+=1
                
        if dico1==dico2:
            return True
        return False
    
test=Solution()
print(test.isAnagram("racecar","carrace"))
print(test.isAnagram("jar","jam"))

