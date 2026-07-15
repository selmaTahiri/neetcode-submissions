class Solution:

    def encode(self, strs):
        res=''
        sizes=[]
        
        for mot in strs:
            sizes.append(len(mot))
        for sz in sizes:
            res+=str(sz)
            res+=','
        res+='#'
        for mot in strs:
            res+=mot
        return res

    def decode(self, s):
        resultat=[]
        sizes=[]
        i=0

        while s[i] != '#':
            current=''
            while s[i] != ',':
                current+=s[i]
                i+=1
            sizes.append(int(current))
            i+=1
        i+=1
        for sz in sizes:
            resultat.append(s[i:i+sz])
            i+=sz
        return resultat

test=Solution()
print(test.encode(["neet","code","love","you"]))
print(test.decode("4,4,4,3,#neetcodeloveyou"))

print(test.encode(["we","say",":","yes"]))
print(test.decode("2,3,1,3,#wesay:yes"))

