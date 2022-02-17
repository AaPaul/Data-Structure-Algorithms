# A very simple way to implement a stack
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []

    def push(self, x: int) -> None:
        self.arr.append(x)
    def pop(self) -> None:
        if self.arr:
            self.arr.pop(-1)
    def top(self) -> int:
        return self.arr[-1]
    def getMin(self) -> int:
        min_element = self.arr[0]
        for i in self.arr[1:]:
            if min_element > i:
                min_element = i
        return min_element
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()