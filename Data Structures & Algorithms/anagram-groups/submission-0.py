class Solution:
    def groupAnagrams(self, strs):
        dictionnaire={}
        for mot in strs:
            cle=''.join(sorted(mot))
            print(cle)
            if cle not in dictionnaire:
                dictionnaire[cle]=[mot]
            else:
                dictionnaire[cle].append(mot)
        return list(dictionnaire.values())

test=Solution()
print(test.groupAnagrams(["act", "cat", "pots", "tops", "stop", "hat"]))