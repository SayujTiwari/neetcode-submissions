class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}
        for num in nums:
            store[num] = store.get(num, 0) + 1
        
        sortedData = dict(sorted(store.items(), key = lambda item: item[1], reverse = True))
        
        output=[]
        count = 0
        for num in sortedData.keys():
            output.append(num)
            count+=1
            if count == k:
                break
        return output 