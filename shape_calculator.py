class Rectangle:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def set_width(self, width: int):
        self.width = width

    def set_height(self, height: int):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width >= 50 or self.height >= 50:
            return "Too big for picture."
        else:
            return self.height * (self.width * '*' + '\n')

    def __str__(self) -> str:
        return 'Rectangle(width={}, height={})'.format(self.width, self.height)

    def get_amount_inside(self, other):
        width_fit= self.width // other.width
        height_fit= self.height // other.height
        return width_fit * height_fit


class Square(Rectangle):

    def __init__(self, side: int):
        super().__init__(side, side)

    def set_side(self, side: int):
        super().set_width(side)
        super().set_height(side)

    def set_width(self, side: int):
        super().set_width(side)
        super().set_height(side)

    def set_height(self, side: int):
        super().set_width(side)
        super().set_height(side)

    def __str__(self) -> str:
        return 'Square(side={})'.format(self.width)

