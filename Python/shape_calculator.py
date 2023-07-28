# Define the Rectangle class
class Rectangle:
    # Constructor to initialize the width and height of the rectangle
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # String representation of the rectangle object
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    # Set the width of the rectangle
    def set_width(self, width):
        self.width = width
    
    # Set the height of the rectangle
    def set_height(self, height):
        self.height = height
    
    # Calculate and return the area of the rectangle
    def get_area(self):
        return (self.width * self.height)

    # Calculate and return the perimeter of the rectangle
    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)
    
    # Calculate and return the diagonal length of the rectangle
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    # Generate a string representation of the rectangle as a picture
    # If the rectangle is too big, it returns "Too big for picture."
    def get_picture(self):
        result = ""
        if self.width > 50 or self.height > 50:
            result = "Too big for picture."
        else:
            for i in range(self.height):
                result += '*' * self.width
                result += "\n"
        
        return result
    
    # Calculate and return the number of shapes that can fit inside the current rectangle
    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)

# Define the Square class, which inherits from Rectangle
class Square(Rectangle):

    # Constructor to initialize the square with a given side length
    def __init__(self, length):
        self.width = length 
        self.height = length
    
    # String representation of the square object
    def __str__(self):
        return f"Square(side={self.width})"
    
    # Set the side length of the square (width and height are the same)
    def set_side(self, length):
        self.width = length
        self.height = length

    # Override the set_height method to set both height and width to the given value
    def set_height(self, height):
        self.width = height
        self.height = height

    # Override the set_width method to set both height and width to the given value
    def set_width(self, width):
        self.width = width
        self.height = width

# Test cases
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))