class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs :
            key = "".join(sorted(string))
            if key in anagrams.keys():
                anagrams[key].append(string)
            else:
                anagrams[key] = [string]
                
        final = []
        for group in anagrams.values():
            final.append(group)
        return final
