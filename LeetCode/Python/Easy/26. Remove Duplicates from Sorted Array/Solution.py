class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        dup = []
        for i in nums:
            if i not in dup:
                dup.append(i)
        for j in range(len(dup)) :
            nums[j] = dup[j]
            
        return len(dup)