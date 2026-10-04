from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = defaultdict(list)

        # Build a dictionary of values:indexes
        for i in range(len(nums)):
            seen[nums[i]] = i

        # for each number, check if the difference is already in the map
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen and seen[diff] != i:
                answer = ([min(seen[diff], i), max(seen[diff], i)])
                # answer = [min(seen[diff], i), max(seen[diff], i)]
                
                
        return answer
                
        