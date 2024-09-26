import random

class RandomizedSet:

    def __init__(self):
        # pass
        self.set = {}

    def insert(self, val: int) -> bool:
        # self.array.append(val)
        isExist = False
        if(self.set.get(val)):
            isExist = True
        # if val exist as key, return false
        # if not exist, create

        if(not isExist):
            self.set[val] = 1
        
        
        return not isExist

    def remove(self, val: int) -> bool:
        # check if exist. 
        isExist = False
        if(self.set.get(val)):
            isExist = True
        if(not isExist):
            return False
        
        # reduce from set. if equal to 0, remove it
        count = self.set.get(val)
        if(count == 1):
            del self.set[val]
        else:
            self.set[val] = count - 1
        return True

    def getRandom(self) -> int:
        keys = list(self.set.keys())
        return random.choice(keys)
        # pass

val = 3
# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(val)
print(param_1)
# param_2 = obj.remove(val)
# print(param_2)
param_3 = obj.getRandom()
print(param_3)