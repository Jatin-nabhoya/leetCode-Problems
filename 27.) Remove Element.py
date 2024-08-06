class Solution:
    def removeElement(self, nums, val: int) -> int:
                        
        # a=[]
        # for i in nums:
        #     if i != val:
        #         a.append(i)
        # return a
        
        a =0
        for i in range(len(nums)):
            
            if nums[i] != val:
                nums[a]=  nums[i]
                a += 1
        return a 
        
        

        # for i in range(len(nums)):
        #     if nums[i] == val:
        #         nums[i] = float('inf')
            
                
        # nums.sort()
        # k = 0
        # for i in range(len(nums)):
        #     if nums[i] == float('inf'):
        #         nums[i] = '_'
        #     else:
        #         k+=1
        # print(nums)
        # return k  

s = Solution()
print(s.removeElement([3,3], 3))
print(s.removeElement([0,1,2,2,3,0,4,2], 2))
print(s.removeElement([3,2,2,3], 3))
print(s.removeElement([0,1,3,0,4,2], 2))