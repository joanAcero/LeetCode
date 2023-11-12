#By Joan Acero Pousa
#Date: 12/11/2021

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l ,r = 0, len(nums)-1
        while l<=r:
            mid = l + (r-l) // 2

            if nums[mid] == target : return True
            
            if nums[l] < nums[mid]: #Left Side
                if nums[l] <= target < nums[mid]:
                    r = mid-1
                else:
                    l = mid +1
            elif nums[l] > nums[mid]: #Right Side
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

            else: #case in which nums[l] = nums[m]
                l += 1
        return False


        

