class Solution:
    def topKFrequent(self, nums, k):
        dico={}
        liste=[]
        resultat=[]
        for nombre in nums:
            if nombre not in dico:
                dico[nombre]=1
            else:
                dico[nombre]+=1
        for keys,values in dico.items():
            liste.append((keys,values))
        print(liste)
        liste.sort(key=lambda x: x[1], reverse=True)
        print(liste)
        for i in range(k):
            resultat.append(liste[i][0])
        return resultat
        
test=Solution()
print(test.topKFrequent([1,2,2,3,3,3], 2))
print(test.topKFrequent([7,7], 1))


