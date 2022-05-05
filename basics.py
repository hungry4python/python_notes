class new:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __mul__(self, other):
        x=self.x * other.x
        y=self.y * other.y
        return new(x,y)
     def __str__(self):
        return "({0},{1})".format(self.x, self.y)
obj=new(5,3)
obj1=new(2,4)
print(obj*obj1)

