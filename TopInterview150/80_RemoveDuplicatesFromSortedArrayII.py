#By Joan Acero Pousa
#Date: 12/11/2021

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(len(nums)):
            if k == 0 or k ==1 or nums[k-2] != nums[i]:
                nums[k] = nums[i]
                k+=1
        return k

                



        