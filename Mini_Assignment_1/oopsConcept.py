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

class SearchCommonElements:
    def __init__(self, s, s1, s2):
        self.s = s
        self.s1 = s1
        self.s2 = s2

    def SearchElements(self):
        res = [];
        dict1 = {};
        dict2 = {}
        for c in list(map(str, self.s)):
            if c in list(map(str, self.s1)):
                if dict1.get(c) is None:
                    dict1[c] = 1
                else:
                    dict1[c] += 1
            if c in self.s2:
                if dict2.get(c) is None:
                    dict2[c] = 1
                else:
                    dict2[c] += 1
                    res = [len(dict1), len(dict2)]
