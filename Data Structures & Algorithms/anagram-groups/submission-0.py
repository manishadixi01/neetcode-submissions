from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resdict = defaultdict(list)
        for word in strs:
            templist = [0]*26
            for ch in word:
                templist[ord(ch) - ord('a')] += 1

            resdict[tuple(templist)].append(word)
        return list(resdict.values())

         