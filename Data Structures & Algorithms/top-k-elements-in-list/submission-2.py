class Solution:
    def topKFrequent(self, nums, k):
        dico={}
        liste=[]
        resultat=[]
        for num in nums:
            if num not in dico:
                dico[num]=1
            else:
                dico[num]+=1
        
        for item in dico.items():
            liste.append(item)
        liste.sort(key=lambda x:x[1], reverse=True)
        
        for i in range(k):
            resultat.append(liste[i][0])
        return resultat
    
test=Solution()
print(test.topKFrequent([1,2,2,3,3,3],2))
print(test.topKFrequent([7,7],1))
