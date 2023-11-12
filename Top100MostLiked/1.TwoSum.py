#By Joan Acero Pousa
#Date: 12/11/2021

class Solution:
    def twoSum(self, nums: List[int], target: int):
        hash_map = {}
        for i in range(len(nums)):
            if target - nums[i] in hash_map:
                return [hash_map[target - nums[i]], i]
            hash_map[nums[i]] = i
        return None
    
   

