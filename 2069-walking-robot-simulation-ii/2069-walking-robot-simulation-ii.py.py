class Robot:

    def __init__(self, width, height):
        self.pos = [((0, 0), "South")]
        for i in range(1, width):
            self.pos.append(((i, 0), "East"))
        for j in range(1, height):
            self.pos.append(((width - 1, j), "North"))
        for i in range(width - 2, -1, -1):
            self.pos.append(((i, height - 1), "West"))
        for j in range(height - 2, 0, -1):
            self.pos.append(((0, j), "South"))
        self.i = 0
        self.isOrigin = True

    def step(self, num):
        self.isOrigin = False
        self.i = (self.i + num) % len(self.pos)

    def getPos(self):
        return self.pos[self.i][0]

    def getDir(self):
        return "East" if self.isOrigin else self.pos[self.i][1]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()