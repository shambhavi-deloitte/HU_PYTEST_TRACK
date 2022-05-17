from itertools import combinations


class StringClass:
    # Constructor
    def __init__(self, s):
        self.s = s

    def lengthOfString(self):
        return len(self.s)

    def ConvertStringToList(self):
        return list(map(str, self.s))

class PairsPossible(StringClass):
    def __init__(self, arr):
        self.arr = arr
        StringClass.__init__(self, arr)

    def StoreAllPossiblePairs(self):
        self.arr = list(combinations(self.s, 2))

    def PrintAllPossiblePairs(self):
        for i in self.arr:
            print(list(i), end=' ')
            print()

    def GetAllPossiblePairs(self):
        return self.arr

    def GetString(self):
        return self.s


# obj = StringClass('12314532')
# print(obj.lengthOfString())
# print(obj.ConvertStringToList())
