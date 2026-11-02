class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map str to  keys and push same str to list
        group = defaultdict(list)

        for st in strs:
            counts = [0] * 26

            for s in st:
              val = ord(s) - ord('a')
              counts[val] += 1
            group[tuple(counts)].append(st)
        
        return list(group.values())