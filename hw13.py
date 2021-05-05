import turtle, math, random

# wn = turtle.Screen()

class Ball(turtle.Turtle):

    def __init__(self, x, y, vx, vy):

        turtle.Turtle.__init__(self)
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.shape("circle")
        self.color("red")
        self.turtlesize(0.3)
        self.penup()
        self.setpos(self.x, self.y)
        self.bounce_count = 0

        turtle.title("Tennis for Two")

    def move(self):
        self.vy = self.vy - 0.981    #Gravity
        self.vx *= 0.99     #Air friction
        self.x = self.xcor()+self.vx
        self.y = self.vy + self.y

        if (self.x < 5) and (self.x > -5):
            self.bounce_count = 0

        if self.y <= 0:
            self.vy = self.vy*(-0.75)
            self.y = 0.75*self.y + (0.75*self.vy)
            self.bounce_count += 1

            if self.bounce_count == 2:
                self.reset()
        else:
            self.y = self.vy + self.ycor()


        self.setpos(self.x, self.y)


    def hit(self):

        self.vx *= -1
        self.vy = 15

    def strong_hit(self):      #Different Hits

        self.vx *= -2.0
        self.vy = 15

    def weak_hit(self):

        self.vx *= -0.5
        self.vy = 15


    def reset(self):
        self.x = random.uniform(-100, 100)
        self.y = random.uniform(30, 100)
        self.vx = random.choice([random.uniform(-12, -6), random.uniform(6, 12)])
        self.vy = random.uniform(4, 10)

        self.setpos(self.x, self.y)
        self.bounce_count = 0




class Game:

    def __init__(self):

        turtle.delay()
        turtle.tracer(0,0)
        turtle.setworldcoordinates(-500, -500, 500, 500)

        #net and court
        turtle.forward(400)
        turtle.left(180)
        turtle.forward(800)
        turtle.left(180)
        turtle.forward(400)
        turtle.left(90)
        turtle.forward(30)
        turtle.hideturtle()

        #background

        #Words
        turtle.penup()
        turtle.goto(-200, 200)
        turtle.pendown()
        turtle.write("Da Sky", move=False, font=("Comic Sans MS", 30, "bold"))

        # Grass
        turtle.bgcolor("deepskyblue")

        # Sky
        turtle.penup()
        turtle.goto(-500, 0)
        turtle.pendown()
        turtle.color("deepskyblue")
        turtle.begin_fill()
        for i in range(2):
            turtle.forward(500)
            turtle.left(90)
            turtle.forward(50)
            turtle.left(90)
        turtle.end_fill()

        # Sun
        turtle.penup()
        turtle.goto(-320, 225)
        turtle.pendown()
        turtle.color("yellow")
        turtle.begin_fill()
        turtle.circle(35)
        turtle.end_fill()

        # Cloud
        turtle.penup()
        turtle.goto(200, 200)
        turtle.pendown()
        turtle.color("white")
        turtle.begin_fill()
        turtle.circle(25)
        turtle.end_fill()

        turtle.penup()
        turtle.goto(220, 240)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(25)
        turtle.end_fill()

        turtle.penup()
        turtle.goto(230, 215)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(25)
        turtle.end_fill()

        turtle.penup()
        turtle.goto(180, 225)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(25)
        turtle.end_fill()

        #Cloud 2
        turtle.penup()
        turtle.goto(300, 300)
        turtle.pendown()
        turtle.color("white")
        turtle.begin_fill()
        turtle.circle(25)
        turtle.end_fill()

        turtle.penup()
        turtle.goto(320, 340)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(25)
        turtle.end_fill()

        turtle.penup()
        turtle.goto(330, 315)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(25)
        turtle.end_fill()

        turtle.penup()
        turtle.goto(280, 325)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(25)
        turtle.end_fill()

        turtle.hideturtle()



        self.ball = Ball(random.randint(-100,100), random.randint(30,100), (random.randint(6,12) * random.choice([1,-1])), (random.randint(4,10)))

        self.ball.move()
        turtle.update()
        self.gameloop()
        turtle.onkeypress(self.ball.hit, "space")
        turtle.onkeypress(self.ball.weak_hit, "b")
        turtle.onkeypress(self.ball.strong_hit, "m")
        turtle.listen()
        turtle.mainloop()


    def gameloop(self):

        if (self.ball.x > -3) and (self.ball.x < 3) and (self.ball.ycor() < 30):
            self.ball.reset()

        turtle.update()
        self.ball.move()
        turtle.ontimer(self.gameloop, 30)


Game()

