class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i1 in range(len(nums)):
            if nums[i1] > target:
                continue

            for i2 in range(i1 + 1, len(nums)):
                if nums[i1] + nums[i2] == target:
                    return [i1, i2]

        return None


stuff = Solution()

print(stuff.twoSum([2, 7, 11, 15], 9))
