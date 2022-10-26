class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        """ METHOD - 1 """
        dict={}
        for i in range(0,len(nums)):
            value=nums[i]
            diff=target-value
            if value not in dict:
                dict[diff]=i
            else:
                curr_index=i
                prev_index=dict[value]
                return [prev_index,curr_index]
    
        """ METHOD - 2 """
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    return [i,j]
    
    
    