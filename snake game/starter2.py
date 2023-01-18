import turtle

# define program constants
WIDTH = 500
HEIGHT = 500
DELAY = 20      

def move_turtle():
    my_turtle.forward(1)
    my_turtle.right(1)
    screen.update()
    screen.ontimer(move_turtle,DELAY)

# create a window where we will do our drawing

screen=turtle.Screen()
screen.setup(WIDTH,HEIGHT)
screen.title('program title')
screen.bgcolor("cyan")
screen.tracer(0)

# Create a turtle to do binding

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("red")

# set animation motion

move_turtle()


turtle.done()