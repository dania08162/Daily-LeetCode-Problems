class Solution(object):
    def twoSum(self, nums, target):
        random_dict = {}
        for x, num in enumerate(nums): 
            number = target - num
            if number in random_dict: 
                return [random_dict[number], x]
            random_dict[num] = x
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
