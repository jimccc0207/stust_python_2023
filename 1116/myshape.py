class myshape:
    def __init__(self,side,length,width,radius):
        self.side = side
        self.length = length
        self.width = width
        self.radius = radius
    def getSquareArea(self):
        return self.side * self.side
    def getRectangleArea(self):
        return self.length * self.width
    def getCircleArea(self):
        return 3.14 * self.radius ** 2

shape=myshape(3, 4, 5, 10)
print(shape.getSquareArea())
print(shape.getRectangleArea())
print(shape.getCircleArea())