class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i in strs:
            sort = "".join(sorted(i))
            if sort in hashmap:
                hashmap[sort].append(i)
            else:
                hashmap[sort] = [i]
        return list(hashmap.values())
    
        
            
                
        
           


        
        