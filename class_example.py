












class Rectangle():
    def __init__(self, length: int, width: int) -> None:
        self.shape_type = "Rectangle"
        self.length = length
        self.width = width
        self.calc_area()
        self.calc_perimeter()
    
    def calc_area(self) -> None:
        self.area = self.length * self.width
        
    def calc_perimeter(self):
        self.perimeter = (self.length * 2) + (self.width * 2)
        
    def print_info(self) -> None:
        print(f"{self.shape_type} Width: {self.width}")
        print(f"{self.shape_type} Length: {self.length}")
        print(f"{self.shape_type} Area: {self.area}")
        print(f"{self.shape_type} Perimieter: {self.perimeter}")
        

if __name__ == "__main__":
    r = Rectangle(5,3)
    r.print_info()