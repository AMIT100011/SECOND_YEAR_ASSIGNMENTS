# Define Image class
class Image:
    # Constructor (default + parameterized)
    def __init__(self, imageWidth=None, imageHeight=None, colorCode=None):
        self.imageWidth = imageWidth
        self.imageHeight = imageHeight
        self.colorCode = colorCode

    # Setter methods
    def set_imageWidth(self, width):
        self.imageWidth = width

    def set_imageHeight(self, height):
        self.imageHeight = height

    def set_colorCode(self, code):
        self.colorCode = code

    # Getter methods
    def get_imageWidth(self):
        return self.imageWidth

    def get_imageHeight(self):
        return self.imageHeight

    def get_colorCode(self):
        return self.colorCode

    # Overriding __str__ method
    def __str__(self):
        return (f"Image Width: {self.imageWidth}, "
                f"Image Height: {self.imageHeight}, "
                f"Color Code: {self.colorCode}")


# Create object using default constructor
img1 = Image()

# Create object using parameterized constructor
img2 = Image(800, 600, "RGB")

# Print details of both objects
print("Image 1 Details:")
print(img1)

print("\nImage 2 Details:")
print(img2)
