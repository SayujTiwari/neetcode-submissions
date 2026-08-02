class TimeMap:

    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []

        self.keyStore[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        times = self.keyStore.get(key, [])

        l, r = 0, len(times) - 1
        result = ""

        while l <= r:
            mid = (l + r) // 2

            if times[mid][0] <= timestamp:
                result = times[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return result