"""
Project: Turtle Scene II
Project Name: FACES (inspired by Chelsea)
CREATED BY: Andrew Stamm
DATE: 4-5-20

The art form for these faces origionally came from my sister Chelsea. 

DESCRIPTION:
This is a program that draws cartoon faces and stick figures using python's turtle module.
These faces and figures are drawn in various scences.
You can select various scenes using argv from the commandline.
The commandline documentation goes as follows:

main.py scene 

Scene Options: scene_one, scene_two, scene_three

WHAT I LEARNED;
In this project, I learned how to tilt and scale complex shapes.
I also learned how to use and set command line parameters as well.
"""

"""
Imports
"""
import turtle
from random import randint
from sys import argv

"""
Location Functions
"""
def goto_xy(pen, x, y):
    """This function picks up a pen, goes to an x, y coordinatate, and puts the pen back down.
        Note: These are absolute x, y locations
    pen (turtle), x (float), y (float) --> None
    """
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

def new_line_forward(pen, length):
    """Given a pen and a length, this function picks up a pen and moves a pen forward without drawing.
    pen (turtle), length (float) --> none
    """
    pen.penup()
    pen.forward(length)
    pen.pendown()

def goto_xy_delta(pen, x_delta, y_delta, tilt=0, scale=1):
    """Given a pen, the change in x (x delta), and the change in y (y delta), this function moves the pen to a new location based off its, current location.
        In other words, this fuction treats the pen's current location as point (0,0), moves the pen left or right a certain x value, and moves the pen up and down a certain y value.
        This function tilts and scales these values as well (optional).
        Note: x_delta, y_delta is a location relative to the pens position.
    pen (turtle), x_delta (flaot), y_delta (float), tilt=0 (float), scale=1 (float) --> none
    """
    pen.penup()
    pen.setheading(tilt)
    pen.forward(x_delta*scale)
    pen.setheading(tilt+90)
    pen.forward(y_delta*scale)
    pen.setheading(tilt)
    pen.pendown()

"""
Shape Functions
"""
def draw_rectangle(pen, width, height):
    """Given the pen, width, and height, this function draws a rectanlge starting at the bottom left corner.
    pen, width, height --> none
    """
    for _ in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)

def draw_star(pen, side_length):
    """Given a pen and side_length, this function draws a five point star.
    pen (turtle), side_length (float) --> none
    """
    for _ in range(5):
        pen.forward(side_length)
        pen.left(-144)
        pen.forward(side_length)
        pen.left(72)

def draw_polynomial_random(pen, perimeter):
    """Given a pen and perimeter, this function draws a random polynomial.
    pen (turtle), perimeter (float) --> none
    """
    sides = randint(3, 7)
    pen.left(180/sides-90)
    for _ in range(sides):
        pen.forward(perimeter/sides)
        pen.left(360/sides)

def draw_triangle_equalateral(pen, side_length):
    """Given a pen and side_length, this function draws an equalateral triangle.
    pen (turtle), side_length (float) --> none
    """
    for _ in range(3):
        pen.forward(side_length)
        pen.left(120)

def draw_circle(pen, radius):
    """Given a pen and radious, this function draws a bow.
    pen (turtle), radius (float) --> none
    """
    new_line_forward(pen, radius)
    pen.left(90)
    pen.circle(radius)

def draw_bow(pen, radius):
    """Given a pen and radious, this function draws a bow.
    pen (turtle), radius (float) --> none
    """
    for i in 0, 180:
        pen.left(i)
        draw_triangle_equalateral(pen, radius)
    r = radius/3
    pen.setheading(0)
    draw_circle(pen, r)

"""
Outline Functions
"""
def draw_outline_cross(pen, x, y, tilt=0, scale=1):
    """Given a pen and an (x, y) coordinate, this function draws an outline of a cross.
        (x,y) is used to line up outliine shapes easily with faces.
        This function can also be tilted and scaled using a tilt and a scale factor (optional).
            tilt is measured in degrees, tilt=0 is North, tilt > 0 rotates counterclockwise, tilt < 0 rotates clockwise
    pen (turtle), x (float), y (float), tilt=0 (float), scale=1 (float) --> None
    """
    width = 210 
    height = 270 
    goto_xy(pen, x, y)
    goto_xy_delta(pen, (-width/2), 0, tilt, scale)
    pen.forward(width * scale)
    goto_xy(pen, x, y)
    goto_xy_delta(pen, 0, (-height/2), tilt, scale)
    pen.left(90)
    pen.forward(height * scale)
    
def draw_outline_star(pen, x, y, tilt=0, scale=1):
    """Given a pen and an (x, y) coordinate, this function draws an outline of a star.
        (x,y) is used to line up outliine shapes easily with faces.
        This function can also be tilted and scaled using a tilt and a scale factor (optional).
            tilt is measured in degrees, tilt=0 is North, tilt > 0 rotates counterclockwise, tilt < 0 rotates clockwise
    pen (turtle), x (float), y (float), tilt=0 (float), scale=1 (float) --> None
    """
    goto_xy(pen, x, y)
    goto_xy_delta(pen, 50, 20, tilt, scale)
    draw_star(pen, 100 * scale)

def draw_outline_square(pen, x, y, tilt=0, scale=1):
    """Given a pen and an (x, y) coordinate, this function draws a square outline.
        (x,y) is used to line up outliine shapes easily with faces. 
        This function can also be tilted and scaled using a tilt and a scale factor (optional).
            tilt is measured in degrees, tilt=0 is North, tilt > 0 rotates counterclockwise, tilt < 0 rotates clockwise
    pen (turtle), x (float), y (float), tilt=0 (float), scale=1 (float) --> None
    """
    goto_xy(pen, x, y)
    goto_xy_delta(pen, -70, -100, tilt, scale)
    pen.left(-10)
    draw_rectangle(pen, 200 * scale, 210 * scale)

def draw_outline_bow(pen, x, y, tilt=0, scale=1):
    """Given a pen and an (x, y) coordinate, this function draws an outline of a cartoon bow.
        (x,y) is used to line up outliine shapes easily with faces.      
        This function can be tilted and scaled using a tilt and a scale factor (optional).
            tilt is measured in degrees, tilt=0 is North, tilt > 0 rotates counterclockwise, tilt < 0 rotates clockwise
    pen (turtle), x (float), y (float), tilt=0 (float), scale=1 (float) --> None
    """
    goto_xy(pen, x, y)
    goto_xy_delta(pen, 20, -8, tilt, scale)
    pen.left(120)
    draw_bow(pen, 150 * scale)

def draw_outline_random(pen, x, y, tilt=0, scale=1):
    """Given a pen and an (x, y) coordinate, this function draws a random polynomial outline.
        (x,y) is used to line up outliine shapes easily with faces.
        This function can be tilted and scaled using a tilt and a scale factor (optional).
            tilt is measured in degrees, tilt=0 is North, tilt > 0 rotates counterclockwise, tilt < 0 rotates clockwise
    pen (turtle), x (float), y (float), tilt=0 (float), scale=1 (float) --> None
    """
    goto_xy(pen, x, y)
    goto_xy_delta(pen, -60, -20, tilt, scale)
    draw_polynomial_random(pen, 700 * scale)

"""
Face and Body Functions
"""
def draw_eyebrows_square(pen, x, y, tilt=0, scale=1):
    """Given a pen and an (x, y) coordinate, this function draws a set of eyebrows made out of eyes.
        This function can be tilted and scaled using a tilt and a scale factor (optional).
            tilt is measured in degrees, tilt=0 is North, tilt > 0 rotates counterclockwise, tilt < 0 rotates clockwise
    pen (turtle), x (float), y (float), tilt=0 (float), scale=1 (float) --> None
    """
    goto_xy(pen, x, y)
    goto_xy_delta(pen, 78, 80, tilt, scale)
    pen.setheading(170 + tilt)
    pen.forward(69*scale)
    pen.setheading(180 + tilt)
    new_line_forward(pen, 25*scale)
    pen.setheading(189 + tilt)
    pen.forward(69*scale)

def draw_eyes_square(pen_eyes, x, y, tilt=0, scale=1):
    """Given a pen and an (x, y) coordinate, this function draws a pair of cartoon eyes made out of rectangles.
        This function can be tilted and scaled using a tilt and a scale factor (optional).
            tilt is measured in degrees, tilt=0 is North, tilt > 0 rotates counterclockwise, tilt < 0 rotates clockwise
    pen (turtle), x (float), y (float), tilt=0 (float), scale=1 (float) --> None
    """
    #initialize eyes: These do not need to be scaled; they will be scaled later on. 
    eye_left_x = -70
    eye_y = 10
    eye_right_x = 10
    pupil_left_x = (eye_left_x + 7)
    pupil_y = (eye_y + 11)
    pupil_right_x = (eye_right_x + 7)
    #Program
    for eye in eye_left_x, eye_right_x:
        goto_xy(pen_eyes, x, y)        
        goto_xy_delta(pen_eyes, eye, eye_y, tilt, scale)
        draw_rectangle(pen_eyes, (50 * scale), (60 * scale))

    for pupil in pupil_left_x, pupil_right_x:
        goto_xy(pen_eyes, x, y)
        goto_xy_delta(pen_eyes, pupil, pupil_y, tilt, scale)
        pen_eyes.begin_fill()
        draw_rectangle(pen_eyes, (28 * scale), (38 * scale))
        pen_eyes.end_fill()    

def draw_nose_square(pen_nose, x, y, tilt=0, scale=1):
    """Given a pen and an (x, y) coordinate, this function draws a cartoon L shaped nose.
        (exclude this function if you are concerned about your face sneezing or are going for a Voldamort_type look)
        This function can be tilted and scaled using a tilt and a scale factor (optional).
            tilt is measured in degrees, tilt=0 is North, tilt > 0 rotates counterclockwise, tilt < 0 rotates clockwise
    pen (turtle), x (float), y (float), tilt=0 (float), scale=1 (float) --> None
    """
    goto_xy(pen_nose, x, y)
    goto_xy_delta(pen_nose, -12, -9, tilt, scale)
    pen_nose.left(-125)
    pen_nose.forward(35 * scale)
    pen_nose.left(97)
    pen_nose.forward(18 * scale)
    
def draw_mouth(pen_mouth, x, y, tilt=0, scale=1):
    """Given a pen and an (x, y) coordinate, this function draws a cartoon half-circle mouth.
        This function can be tilted and scaled using a tilt and a scale factor (optional).
            tilt is measured in degrees, tilt=0 is North, tilt > 0 rotates counterclockwise, tilt < 0 rotates clockwise
    pen (turtle), x (float), y (float), tilt=0 (float), scale=1 (float) --> None
    """
    goto_xy(pen_mouth, x, y)
    goto_xy_delta(pen_mouth, -44, -90, tilt, scale)
    pen_mouth.begin_fill()
    pen_mouth.left(-54)   
    pen_mouth.circle((49 * scale), 150)
    pen_mouth.left(104)
    pen_mouth.forward(95.327777 * scale)
    pen_mouth.end_fill()

def draw_body_main(pen, x, y, tilt=0, scale=1):
    """Given a pen and an (x, y) coordinate, this function draws a stick figure body with circles for the hands and rectangles for the feet.
        This function can be tilted and scaled using a tilt and a scale factor (optional).
            tilt is measured in degrees, tilt=0 is North, tilt > 0 rotates counterclockwise, tilt < 0 rotates clockwise
    pen (turtle), x (float), y (float), tilt=0 (float), scale=1 (float) --> None
    """  
    #draw body and legs
    leg_radius = 160 * scale
    for r in -leg_radius, leg_radius:
        goto_xy(pen, x, y)
        goto_xy_delta(pen, 4, -135, tilt, scale)
        pen.left(-90)
        pen.forward(150 * scale)
        pen.circle(-r, 30)
        pen.circle(r, 30)
        pen.forward(50 * scale)
        pen.left(-90)
        pen.begin_fill()
        draw_rectangle(pen, 25 * scale, 10 * scale)
        pen.end_fill()
    #draw arms
    for angle in 0, 180:
        goto_xy(pen, x, y)
        goto_xy_delta(pen, 4, -185, tilt, scale)
        pen.left(angle)
        pen.circle((-100 * scale), 60)
        pen.begin_fill()
        draw_circle(pen, 10 * scale)
        pen.end_fill()

"""
Faces
"""
#Again, I origionally intended to draw more faces.
def draw_face_main(pen, x, y, tilt=0, scale=1):
    """Given a pen and an (x, y) coordinate, this function draws the main (original) face.
        This function can be tilted and scaled using a tilt and a scale factor (optional).
            tilt is measured in degrees, tilt=0 is North, tilt > 0 rotates counterclockwise, tilt < 0 rotates clockwise
    pen (turtle), x (float), y (float), tilt=0 (float), scale=1 (float) --> None
    """
    draw_eyes_square(pen, x, y, tilt, scale)
    draw_nose_square(pen, x, y, tilt, scale)
    draw_mouth(pen, x, y, tilt, scale)
    draw_eyebrows_square(pen, x, y, tilt, scale)

"""
Person Function
"""
#This function behaves as if I had made multiple faces even though I only made one.
def draw_person(pen, x, y, tilt=0, scale=1, face=draw_face_main):
    """Given a pen and an (x, y) coordinate, this function draws a person using a face function and draw_body_main()
        This function can be tilted and scaled using a tilt and a scale factor (optional).
            tilt is measured in degrees, tilt=0 is North, tilt > 0 rotates counterclockwise, tilt < 0 rotates clockwise
            Default scale for this function is scale=.5 because it's size.
        This function also accepts a face function (functions listed under "faces') as an arguement (optional).
            If no face function is given, face=draw_face_main.
    pen (turtle), x (float), y (float), tilt=0 (float), scale=.5 (float) face=draw_face_main (face function) --> None
    """
    s = .5 * scale
    face(pen, x, y, tilt, s)
    draw_body_main(pen, x, y, tilt, s)
    

"""
Scenes
"""
def draw_scene_floor(pen, screen_width, screen_height):
    """Given a pen, screen_width, and a screen height, this function draws a "floor" for the scene using a rectangle
    pen (turtle), screen_width (float), screen_height(float) --> none
    """
    pen.color(color_schemes["gray"][0])
    pen.setheading(0)
    goto_xy(pen, -screen_width/2, -screen_height/2)
    pen.begin_fill()
    draw_rectangle(pen, screen_width, screen_height/5)
    pen.end_fill()

def draw_scene_rectangle(pen, x, y, tilt=0, scale=1):
    """Given a pen and an (x, y) coordinate, this function draws an outline of a rectangle (this rectangle goes around scene_one during scene_two).
        This function can be tilted and scaled using a tilt and a scale factor (optional).
            tilt is measured in degrees, tilt=0 is North, tilt > 0 rotates counterclockwise, tilt < 0 rotates clockwise
    pen (turtle), x (float), y (float), tilt=0 (float), scale=1 (float) --> None
    """
    pen.color(color_schemes["black"][2])
    width=500 * scale
    height=350 * scale
    goto_xy(pen, x, y)
    goto_xy_delta(pen, -width/2, -height/2, tilt, scale)
    draw_rectangle(pen, width, height)

def scene_one(x=None, y=None, main_scene=True, scale=1):
    """This function draws the original snence I made for project three, but with a twist.
        Given an x, y coordinate and a scale value, this function can be moved and scaled.
        If main_scene is True, this function will change the screen size.
    x=None (float), y=None (float), main_scene=True (boolean), scale=1 (float) --> none
    """
    #Pen and Screen_set_up
    if main_scene == True:
        pen_face.showturtle()
        pen_cross.speed(9.5)
        pen_outline.speed(9.5)
        screen_width = 1000 * scale
        screen_height = 700 * scale
        turtle.Screen().setup(screen_width, screen_height)
    #Point_set_up
    main_x, main_y= 275 * scale, 175 * scale
    point_list = [[0, 0],[main_x, main_y],[-main_x, main_y],[-main_x, -main_y],[main_x, -main_y]]
    if x and y != None:
        for i in range(len(point_list)):
            point_list[i][0], point_list[i][1] = point_list[i][0] + x, point_list[i][1] + y
    #Cue_set_up
    cue_colors = [color_schemes["black"], color_schemes["gold"], color_schemes["red"], color_schemes["pink"], color_schemes["blue"]]
    cue_outlines = [draw_outline_square, draw_outline_star, draw_outline_random, draw_outline_bow, draw_outline_random]
    cue_orders = [[2, 1, 4, 0, 3], [0, 1, 3, 4, 2], [4, 2, 3, 1, 0]]
    # draw_scene_outlines
    for i in cue_orders[0]:
        pen_outline.color(cue_colors[i][2])
        cue_outlines[i](pen_outline, point_list[i][0], point_list[i][1], scale=scale)
    # draw_scene_crosses
    for i in cue_orders[1]:
        draw_outline_cross(pen_cross, point_list[i][0], point_list[i][1], tilt=randint(-10,10), scale=scale)
    # draw_scene_faces
    for i in cue_orders[2]:
        pen_face.color(cue_colors[i][0], cue_colors[i][1])
        draw_face_main(pen_face, point_list[i][0], point_list[i][1], tilt=randint(-9, 9), scale=scale)
    pen_face.hideturtle()

def scene_two():
    """This function draws a scene comprizing of several people and shapes.
        Scene one is included in this scene as well.
    none --> none
    """
    #Screen Set Up
    screen_width = 1000
    screen_height = 750
    turtle.Screen().setup(screen_width, screen_height)
    #Outline Cue Set Up
    point_list_side = [[370, 260], [170, 130], [360, 0], [170, -130]]
    cue_colors = [color_schemes["gold"], color_schemes["pink"], color_schemes["black"], color_schemes["blue"]]
    cue_outlines = [draw_outline_star, draw_outline_bow, draw_outline_square, draw_outline_random]
    #Draw_scene_outlines
    for point in range(len(point_list_side)):
        draw_outline_cross(pen_cross, point_list_side[point][0], point_list_side[point][1], scale=.75)
    for point in range(len(point_list_side)):
        pen_outline.color(cue_colors[point][2])
        cue_outlines[point](pen_outline, point_list_side[point][0], point_list_side[point][1], scale=.8)
    draw_scene_floor(pen_outline, screen_width, screen_height)
    #Draw scene People
    xs = [270, 100, -70, -240]
    cue_colors = [color_schemes["blue"], color_schemes["gold"], color_schemes["green"], color_schemes["red"]]
    for i in range(len(xs)):
        pen_face.color(cue_colors[i][0], cue_colors[i][1])
        draw_person(pen_face, xs[i], -100)
    #Draw Scene One 
    draw_scene_rectangle(pen_outline, -220, 160, tilt=4)
    scene_one(-220, 160, False, .5)
    #Draw Giant
    pen_face.color(color_schemes["black"][0], color_schemes["black"][1])
    draw_person(pen_face, 280, 180, tilt=35, scale=2.5)
    # hide objects and finish up
    pen_cross.reset()
    pen_cross.hideturtle()

def scene_three():
    """This function draws a single stick figure.
    none --> none
    """
    turtle.Screen().setup(700, 1000)
    draw_scene_floor(pen_outline, 700, 1000)
    draw_person(pen_face, 0, 150, scale=2)

"""
Main
"""
color_schemes = {
    "red": ("#990000" , "#d60000", "#ffc999"),
    "gold": ("#d67d00", "#edb200", "gold"),
    "blue": ("#001000", "#001685", "#53f9fc"),
    "pink": ("#d100b2", "#5e0094", "pink"),
    "black": ("#000000", "#000000", "#aaaaaa"),
    "green": ("#006824", "#00f800", "#32f87d"),
    "gray": ("#e1e1e1", "#ffffff", "#e1e1e1")
}

pen_face = turtle.Turtle()
pen_face.pensize(2)
pen_face.speed(0)
pen_face.hideturtle()

pen_outline = turtle.Turtle()
pen_outline.speed(0)
pen_outline.hideturtle()

pen_cross = turtle.Turtle()
pen_cross.speed(0)
pen_cross.hideturtle()
pen_cross.color("#999999")

def main():
    """This is where the program begins
    """
    scenes = {
        "scene_one": scene_one,
        "scene_two": scene_two,
        "scene_three": scene_three
    }
    scene = scene_two

    if len(argv) == 2:
        scene = scenes[argv[1]]
    scene()
    turtle.done()

def template():
   # draw_outline_cross(pen_cross, 0, 0)
    draw_face_main(pen_face, 0, 0)

def draw_face_star():
    goto_xy_delta(pen_face, -40, 52)
    draw_star(pen_face, 30)
    # pen_face.left(30)
    pen_face.forward(70)

def bow():
    draw_outline_bow(pen_face, 100, 100, tilt=-20, scale=.4)
    draw_face_main(pen_face, 0, 0)
    turtle.done()


if __name__ == "__main__":
    main()