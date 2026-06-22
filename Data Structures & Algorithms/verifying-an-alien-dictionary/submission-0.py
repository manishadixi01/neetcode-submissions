class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien_list = list(order)
        alien_dict = {}
        for index, element in enumerate(alien_list):
            alien_dict[element] = index
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            for j in range(len(w1)):
                if j == len(w2):
                    return False
                if w1[j] != w2[j]:
                    if alien_dict[w1[j]] > alien_dict[w2[j]]:
                        return False
                    break
        return True


        