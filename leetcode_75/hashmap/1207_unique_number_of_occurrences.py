class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap={}

        
        for ix,val in enumerate(arr):
            hashmap[val]=hashmap.get(val,0)+1
        return len(hashmap.values())==len(set(hashmap.values()))

