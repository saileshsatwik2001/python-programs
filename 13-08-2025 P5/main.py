from b.geometry import Rectangle, Square, Triangle

rect = Rectangle(5, 3)
print("Rectangle - Area:", rect.area(), "Perimeter:", rect.perimeter())

sq = Square(4)
print("Square - Area:", sq.area(), "Perimeter:", sq.perimeter())

tri = Triangle(6, 4, 5, 5, 6)
print("Triangle - Area:", tri.area(), "Perimeter:", tri.perimeter())