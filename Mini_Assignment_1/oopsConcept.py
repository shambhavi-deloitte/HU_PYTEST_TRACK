from itertools import combinations


class StringClass:
    # Constructor
    def __init__(self, s):
        self.s = s

    def lengthOfString(self):
        return len(self.s)

    def ConvertStringToList(self):
        return list(map(str, self.s))




# obj = StringClass('12314532')
# print(obj.lengthOfString())
# print(obj.ConvertStringToList())
