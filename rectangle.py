class Rectangle:
    def __init__(self,length,width):
        self.l=length
        self.w=width
    def area(self):
        print("area =",self.l*self.w)
    def perimeter(self):
        print("Perimeter =",2*(self.l+self.w))
c=Rectangle(10,20)
c.area()
c.perimeter()