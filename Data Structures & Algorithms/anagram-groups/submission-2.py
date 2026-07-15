class Solution:
    def groupAnagrams(self, strs):
        liste=[]
        dico={}
        for mot in strs:
            cle=''.join(sorted(mot))
            if cle not in dico:
                dico[cle]=[mot]
            else:
                dico[cle].append(mot)
        for value in dico.values():
            liste.append(value)
        return liste
        
    
test=Solution()
print(test.groupAnagrams(["act","pots","tops","cat","stop","hat"]))
print(test.groupAnagrams(["x"]))
print(test.groupAnagrams([""]))

