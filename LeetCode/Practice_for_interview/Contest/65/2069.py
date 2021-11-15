from typing import List
class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.pos = [0, 0]
        self.direction = "East"
        # self.direction_dict = {
        #                         0: "East",
        #                         90: "North",
        #                         180: "West",
        #                         270: "South"
        #                     }

    def move(self, num: int) -> None:
        if num == 0:
            return 
        x, y = self.pos
        if self.direction == "East":
            if x + num < self.width:
                x += num
                self.pos = [x, y]
            else:
                num -= self.width - x - 1
                x = self.width - 1
                self.pos = [x, y]
                self.direction = "North"
                self.move(num)
        elif self.direction == "North":
            if y + num < self.height:
                y += num
                self.pos = [x, y]
            else:
                num -= self.height - y - 1
                y = self.height - 1
                self.pos = [x, y]
                self.direction = "West"
                self.move(num)
        elif self.direction == "West":
            if x - num >= 0:
                x -= num
                self.pos = [x, y]
            else:
                num -= x
                x = 0
                self.pos = [x, y]
                self.direction = "South"
                self.move(num)
        else:
            if y - num >= 0:
                y -= num
                self.pos = [x, y]
            else:
                num -= y
                y = 0
                self.direction = "East"
                self.move(num)

    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        return self.direction


# Your Robot object will be instantiated and called as such:
# obj = Robot(6, 3)
# obj.move(2)
# obj.move(2)
# print(obj.getPos())
# print(obj.getDir())
# obj.move(2)
# obj.move(1)
# obj.move(4)
# print(obj.getPos())
# print(obj.getDir())
obj = Robot(20, 13)
obj.move(12)
obj.move(21)
print(obj.getPos())
print(obj.getDir())
obj.move(17)
print(obj.getPos())
print(obj.getDir())