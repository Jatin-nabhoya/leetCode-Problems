class Solution:
    def removeDuplicates(self, nums) -> int:  
        j=0
        for i in range(len(nums)):
            print(f" j : {nums[j]}")
            if nums[i] !=  nums[i-1]:
                nums[j] =nums[i]
                j+=1
                print(nums)
        return j
              
            

s = Solution()
print(s.removeDuplicates([-1,0,0,0,1,1,2,3,3,3,3,4,4,5,5,6,7,8,8,9,9,9]))