class Solution:
    def productExceptSelf(self, nums):
        liste=[]
        for i in range(len(nums)):
            multi=1
            for j in range(len(nums)):
                if i!=j:
                    multi=multi*nums[j]
            liste.append(multi)
        return liste
    
    
test=Solution()
print(test.productExceptSelf([1,2,4,6]))
print(test.productExceptSelf([-1,0,1,2,3]))
