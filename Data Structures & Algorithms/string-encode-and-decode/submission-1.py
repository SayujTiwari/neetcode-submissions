class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes, res = [], []
        for s in strs:
            sizes.append(len(s))
        for sz in sizes:
            res.append(str(sz))
            res.append(',')
        res.append('#')
        res.extend(strs)
        return ''.join(res)
    def decode(self, s: str) -> List[str]:
        sizes = ""
        indexNum = 0
        for i in range(len(s)):
            if s[i] != "#":
                sizes += s[i]
                
            else:
                indexNum = i + 1
                break
        sizes = sizes.split(",")

        decodedArr = []
        for num in sizes[:-1]:
            num = int(num)
            decodedArr.append(s[indexNum:indexNum+num])
            indexNum = indexNum+num
        
        return decodedArr
