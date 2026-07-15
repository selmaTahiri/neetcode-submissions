class Solution:
    def groupAnagrams(self, strs):
        dico={}
        liste=[]
        for mot in strs:
            cle=''.join(sorted(mot))
            print(cle)
            if cle not in dico:
                dico[cle]=[mot]
            else:
                dico[cle].append(mot)
        for values in dico.values():
            liste.append(values)
        return liste
        
test=Solution()
print(test.groupAnagrams(["act", "cat", "pots", "tops", "stop", "hat"]))

