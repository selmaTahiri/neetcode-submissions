class Solution:

    def encode(self, strs):
        sizes=[]
        code=''
        for mot in strs:
            sizes.append(len(mot))
        for sz in sizes:
            code+=str(sz)
            code+=','
        code+='#'
        for mot in strs:
            code+=mot
        return code
    
    def decode(self, s):
        resultat=[]
        sizes=[]
        i=0
        while s[i] != '#':
            current=''
            while s[i] != ',':
                current+=s[i]
                print(current)
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
print(test.decode('4,4,4,3,#neetcodeloveyou'))
print(test.encode(["we","say",":","yes","!@#$%^&*()"]))
print(test.decode('2,3,1,3,10,#wesay:yes!@#$%^&*()'))

