from random import randint
import turtle

# Project to find if the given co-ordinates are with the rectangle co-ordinates.

class Point:

    def __init__(self, x,y):
        #print("I am init function")
        self.x = x
        self.y = y

    def falls_in_rectangele(self, rectangle):
        #print("I am main function")
        if rectangle.lowleft.x < self.x < rectangle.upright.x\
            and rectangle.lowleft.y< self.y < rectangle.upright.y:
            return True
        else:
            return False




class Rectangle:

    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright

    def rectangleArea(self):
        return (self.upright.x - self.lowleft.x) * (self.upright.y - self.lowleft.y)



class Canvas(Rectangle):

    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.lowleft.x, self.lowleft.y)
        canvas.pendown()

        canvas.forward(self.upright.x - self.lowleft.x)
        canvas.left(90)

        canvas.forward(self.upright.y - self.lowleft.y)
        canvas.left(90)

        canvas.forward(self.upright.x - self.lowleft.x)
        canvas.left(90)
        canvas.forward(self.upright.y - self.lowleft.y)

        #turtle.done()


class CanvasPoint(Point):
# this shows a dot for user result of rectangl area.
    def draw(self, canvas, size=10, color='red'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)



# showing results

rectangle = Canvas(
    Point(randint(0,400), randint(0,400)),
    Point(randint(10,400), randint(10,400))
)

print("Rectangle Coordinates: ",
        (rectangle.lowleft.x,
        rectangle.lowleft.y,), "and",
        (rectangle.upright.x,
        rectangle.upright.y))

user_points = CanvasPoint(float(
    input("Guess X: ")),float(input("Guess Y: ")))


print("Your points are inside the rectangel: ", user_points.falls_in_rectangele(rectangle))


user_area = float(input("Guess the rectangle area: "))

if user_area == rectangle.rectangleArea():
    print(f"Correct..! Your area guess {user_area} is right. ")
else:
    print("Incorrect..! Your area guess was off by: ",
        rectangle.rectangleArea() - user_area)


myturtle = turtle.Turtle()
rectangle.draw(canvas=myturtle)
user_points.draw(canvas=myturtle)
turtle.done()