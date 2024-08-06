from typing import List

class Solution:
    def canBeEqual(self, target, arr: List[int]) -> bool:
        target.sort()
        arr.sort()
        if target==arr:
            return True
        else: 
            return False
    
s = Solution()
print(s.canBeEqual([3,7,9], [3,7,11]))
print(s.canBeEqual([7], [7]))
