class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        counter = 0 

        for each in nums:
            if each != val:
                nums[counter] = each
                counter += 1

        return counter        