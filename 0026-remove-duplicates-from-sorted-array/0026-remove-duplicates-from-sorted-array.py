class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i , j, n = 0,1, len(nums)
        while j < n:
            if nums[j] != nums[i]:
                i = i + 1
                nums[i] = nums[j]
                
            j = j+1
        return i+1 