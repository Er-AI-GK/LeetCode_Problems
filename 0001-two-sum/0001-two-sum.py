class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        """ METHOD - 1 """
        prev = {}
        for i, v in enumerate(nums):
            remaining = target - nums[i]
            if remaining in prev:
                return [i, prev[remaining]]
            
            prev[v] = i
    
        """ METHOD - 2 """
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    return [i,j]
    
    
    