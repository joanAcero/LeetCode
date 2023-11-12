#By Joan Acero Pousa
#Date: 12/11/2021

from typing import List 

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        nums.sort()
        c = 0
        #create hashmap with candidates and counts
        candidates = {}

        majority = len(nums) / 2
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                c +=1
                if c <= majority: candidates[nums[i]] = c
            else: c=0
        
        return max(candidates, key=candidates.get)
        

if __name__ == "__main__":
    s = Solution()
    nums = [2,2,1,1,1,2,2]
    print(s.majorityElement(nums))
