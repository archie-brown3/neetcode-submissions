from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list)

        # build hashmap first
        for i in range(len(strs)):
            sorted_key = "".join(sorted(strs[i]))
            
            anagrams[sorted_key].append(strs[i])
            
            # turn the hashmap into a list
        answer = []
        for group in anagrams.values():
            answer.append(group)


        return answer
        