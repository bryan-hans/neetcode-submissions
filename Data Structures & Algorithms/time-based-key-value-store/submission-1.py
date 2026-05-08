class TimeMap:

    def __init__(self):
        self.store = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])

        l, r = 0, len(values) - 1

        while l <= r:
            middle = (l + r) // 2
            if values[middle][1] <= timestamp:
                res = values[middle][0]
                l = middle + 1 
            else:
                r = middle - 1
        
        return res



        
