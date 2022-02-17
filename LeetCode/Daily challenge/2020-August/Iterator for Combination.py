# The good way to implement the combination calculation in Python is to use 'itertools'
# With order, we should call `itertools.permutations()`.
# Without order, we should use `itertools.combinations()`.


import itertools

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        # self.characters = characters
        # self.combinationLength = combinationLength
        # self.count = 0
        self.combine = list("".join(list(i)) for i in itertools.combinations(characters, combinationLength))

    def next(self) -> str:
        return self.combine.pop(0)

    def hasNext(self) -> bool:
        if self.combine:
            return True
        else:
            return False

# Your CombinationIterator object will be instantiated and called as such:
obj = CombinationIterator('abc', 3)
print(obj.next())
print(obj.hasNext())