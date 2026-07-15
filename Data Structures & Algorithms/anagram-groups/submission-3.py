class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l=[]
        d={}
        for mot in strs:
            cle = "".join(sorted(mot))
            if cle not in d:
                d[cle]=[mot]
            else:
                d[cle].append(mot)

        for value in d.values() :
            l.append(value)
        return l