from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(list)

        # initialise hashmap 
        for i in range(len(nums)):
            # key = int, value = indicies
            seen[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if seen[diff] and i != seen[diff]:
                answer = sorted([i, seen[diff]])
        
        print(answer)
        return(answer)
        