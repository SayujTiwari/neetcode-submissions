class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = []
        for word in strs:
            sortedWord = "".join(sorted(word))
            store.append(sortedWord)

        output = {}
        
        for i in range(len(store)):
            if output.get(store[i]) is None:
                output[store[i]] = [strs[i]]
            else:
                output[store[i]].append(strs[i])
        return list(output.values())