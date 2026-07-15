class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        liste=[]
        for i in range(len(nums)):
            multiplication=1
            for j in range(len(nums)):
                if i!=j:
                    multiplication=multiplication*nums[j]
            liste.append(multiplication)
        return liste

test=Solution()
print(test.productExceptSelf([1,2,4,6]))
print(test.productExceptSelf([-1,0,1,2,3]))