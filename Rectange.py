class Rectangele:
    def __init__(self,l,w) -> None:
        self.__length=l
        self.__width=w
        self.myname='joy'
    def __perimeter(self):
        return 2*(self.__length+self.__width)
    def __area(self):
        return (self.__length*self.__width)
    def display(self):
        print('length of the rectangle: ',self.__length)
        print('width of the rectangle: ',self.__width)
        print('area of the rectange ',self.__area())
        print('perimeter of the rectangle ',self.__perimeter())


rectangle_object=Rectangele(3,4)
rectangle_object.display()
print(rectangle_object.myname)
    