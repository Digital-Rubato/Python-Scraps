#Examples on superclasses (super())


#2 classes to illustrate super classes. Note the repetitive tasks of both classes. Could it be solved simply? 
class Rectangle:
	def __init__(self, length, width):
		self.length = length
		self.width = width

	def area(self):
		return self.length * self.width
	
	def perimeter(self):
		return 2 * self.length + 2 * self.width

class Square:
	def __init__(self, length):
		self.length = length

	def area(self):
		return self.length * self.length

	def perimeter(self):
		return 4 * self.length

square = Square(4)
print("this is the area of the first square: ",square.area())

rectangle = Rectangle(2,4)
print("This is the area of the rectangle: ",rectangle.area())

# now with super() 
#super uses the inheritance property to reduce the amount of code written

class Rectangle:
	def __init__(self, length, width):
		self.length = length
		self.width = width

	def area(self):
		return self.length * self.width

	def perimeter(self):
		return 2 * self.length + 2 * self.width

#Here we declare that the Square class inherits from the Rectangle class

class Square(Rectangle):
	def __init__(self, length):
		super().__init__(length, length)

square = Square(4)
print("This is square after super(): ", square.area())

#super can also call the methods iof the superclass into the subclass


class Square(Rectangle):
	def __init__(self, length):
		super().__init__(length, length)

class Cube(Square):
	def surface_area(self):
		face_area = super().area()
		return face_area * 6

	def volume(self):
		face_area = super().area()
		return face_area * self.length

#super() returns a delegate object to a parent class, so you call the method you want directly on it: super().area()
#this allows us to change the internal .area() logic in a single location. This is handy when you have a number of subclasses inheriting from one superclass

cube = Cube(3)
print("This is cube.surface_area(): ", cube.surface_area())

print("This is cube.volume(): ", cube.volume())

