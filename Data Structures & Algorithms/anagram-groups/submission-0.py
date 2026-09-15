class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      a={}
      for i in range(len(strs)):
        key="".join(sorted(strs[i])) #act

        if key not in a:
            a[key]=[strs[i]]
        else:
            a[key].append(strs[i])
        
      return list(a.values())
    



        