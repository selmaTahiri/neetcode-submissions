class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[]
        for i in range (len(nums)):
            for j in range (i+1, len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    l.append(min(i, j))
                    l.append(max(i, j))
                    return l