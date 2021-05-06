import random, turtle


class Shape:
    '''
    Purpose: an object of this class represents the characteristics (color and dimensions) of the shape
    Instance variables: .x for the x coordinate, .y for the y coordinate, . color for the color of the shape
    Methods: none
    '''

    def __init__(self, x=0, y=0,):
        width = 20
        height = 20
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = random.choice(["red", "orange", "yellow",
                                    "green", "blue", "purple"])

    def __str__(self):
        loc = "(x=" + str(self.x) + ", y=" + str(self.y) + "), "
        col = self.color
        return loc + col


class Circle(Shape):
    '''
    Purpose: an object of the this class in specifically for a circle. It draws a circle.
    Instance variables: .rad
    Methods: (What methods does this class have, and what does each do in a few words?)
    '''

    def __init__(self, x=0, y=0, rad=0):
        Shape.__init__(self, x, y)
        self.rad = rad

    def __str__(self):
        shape_str = Shape.__str__(self)
        return shape_str + ", rad=" + str(self.rad)

    def draw(self, t):
        t.penup()
        t.setpos(self.x, self.y - self.rad)
        t.pendown()
        t.fillcolor(self.color)
        t.begin_fill()
        t.circle(self.rad)
        t.end_fill()


class Rectangle(Shape):
    def __init__(self,x,y, width=20, height=20):
        Shape.__init__(self, x, y)
        self.width = width
        self. height = height

    def __str__(self):
        shape_str = Shape.__str__(self)
        return '(x={}, y={}), color, w:{}, h:{}'.format(x,y,width,height)

    def draw(self, t):
        t.penup()
        t.setpos(self.x, self.y)
        t.pendown()
        t.fillcolor(self.color)
        t.begin_fill()

        w = random.randint(10,50)
        h = random.randint(10,50)

        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)

        t.end_fill()




class Display:
    def __init__(self):
        self.shapes = []
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.hideturtle()
        turtle.delay(0)
        turtle.onscreenclick(self.mouse_event)
        turtle.listen()
        turtle.mainloop()  # Required for some IDEs

    def mouse_event(self, x, y):
        fifty_fifty = random.choice([0,1])

        if fifty_fifty == 0:
            new_circ = Circle(x, y, random.randint(10, 50))
            self.shapes.append(new_circ)
            new_circ.draw(self.t)
        else:
            new_rectangle = Rectangle(x, y, random.randint(10,50), random.randint(10,50))
            self.shapes.append((new_rectangle))
            new_rectangle.draw((self.t))


Display()
