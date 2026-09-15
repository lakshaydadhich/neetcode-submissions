class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a={}
        for word in strs:
            count=[0]*26
            for chr in word:
                count[ord(chr)-ord('a')]+=1
            key=tuple(count)
            if key not in a:
                a[key]=[word]
            else:
                a[key].append(word)

        return list(a.values())