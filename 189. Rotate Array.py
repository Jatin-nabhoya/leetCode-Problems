class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n  # In case the steps are greater than the length of the array
        nums[:] = nums[-k:] + nums[:-k]
        return nums
        
s = Solution()
print(s.rotate([1,2,3],4))  
        