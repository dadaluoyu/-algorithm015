#leetcode_1 两数之和

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, k in enumerate(nums):
            if hashmap.get(target - k) is not None:
                return [i,hashmap.get(target - k)]
            hashmap[k] = i
            #k是key i是value下标