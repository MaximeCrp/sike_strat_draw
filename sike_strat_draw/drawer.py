import turtle
import canvasvg
import datetime

"""
sike_strat_drawer module
========================

This module is meant to be a tool to allow easier representation of isogenies computations in the form of trees.
It can be used in the SIKE protocol context to represent different computation strategies.

Class
-----
Drawer : 
    the very class used to handle the screen and graph. It uses the turtle module implemented thanks to tkinter canvas


Dependencies
------------
turtle :
    module used to actually draw the graph
canvasvg :
    community tool to save tkinter canva into a svg file
datetime :
    for default file name saving with current date and time
    
:Example:

>> from sike_strat_draw import drawer
>> import random
>> dw = drawer.Drawer()
>> dw.init_drawing()
>> dw.save_point(0, 0)
>> dw.draw_isogeny()
>> dw.draw_final_dot()
>> dw.restore_point(0, 0)
>> dw.draw_doubling()
>> dw.draw_final_dot()
>> dw.end_tree()
>> dw.save_drawing()
>> dw.end_drawing()

"""


class Drawer:
    """
        A class used to draw isogenic strategy trees. Refer to SIKE protocol documentation

        ...

        Attributes
        ----------
        :param tree_angle: default 30, in degrees, (half) the angle between each branch split
        :param arrow_length: default 50, the length of each branch. Needs to be small for large trees
        :param arrow_head_length: default 5, the length of the head of each branch as an arrow
        :param arrow_head_angle: default 135, in degrees, the angle for arrow head representation
        :param dot_radius: default 4, radius of dots drawn to represent elliptic curve points
        :param isogeny_color: default "red", color of branches representing isogeny computations
        :param doubling_color: default "blue", color of branches representing doubling computations
        :param dot_color: default "black", color of standard dots representing standard points
        :param final_dot_color: default "green", color of dots representing destination points
        :param screen_width_ratio: default 1.0, floating number for screen width ratio
        :param screen_height_ratio: default 1.0, floating number for screen height ratio
        :param drawing_speed: default 20, integer driving the pace of drawing
        :param save_file_name: default None, custom file name for canvas saving, defaults to current date/time

        Methods
        -------
        save_point(row, index)
            Saves graph coordinates for (row, index) elliptic curve point

        restore_point(row, index)
            Moves drawing coordinates to previously saved (row, index) curve point

        init_drawing()
            Initiates screen, turtle and first point

        _init_isogeny()
            Initiates color and branch splitting for isogeny

        _init_doubling()
            Initiates color and branch splitting for isogeny

        _init_arrow()
            Moves outside previous dot before drawing arrow

        _draw_arrow()
            Draws arrow in previously set position, angle and color

        _draw_dot()
            Draws standard dot

        draw_isogeny()
            Sets correct angle and color then draws isogeny arrow

        draw_doubling()
            Sets correct angle and color then draws doubling arrow

        draw_final_dot()
            Draws dot corresponding to destination curve point

        end_tree()
            Hides turtle drawer at the end

        save_drawing()
            Saves whole canvas to a file with name set to save_file_name

        end_drawing()
            Static method. Ends drawing session
        """

    def __init__(
        self,
        tree_angle=30,
        arrow_length=50,
        arrow_head_length=5,
        arrow_head_angle=135,
        dot_radius=4,
        isogeny_color="red",
        doubling_color="blue",
        dot_color="black",
        final_dot_color="green",
        screen_width_ratio=1.0,
        screen_height_ratio=1.0,
        drawing_speed=20,
        save_file_name=None
    ):
        self.turtle_size = 20
        self.tree_angle = tree_angle
        self.arrow_length = arrow_length
        self.arrow_head_length = arrow_head_length
        self.arrow_head_angle = arrow_head_angle
        self.dot_radius = dot_radius

        self.isogeny_color = isogeny_color
        self.doubling_color = doubling_color
        self.dot_color = dot_color
        self.final_dot_color = final_dot_color
        
        self.screen_width_ratio = screen_width_ratio
        self.screen_height_ratio = screen_height_ratio
        self.drawing_speed = drawing_speed

        self.save_file_name = save_file_name

        self.number_isogenies = 0
        self.number_doubling = 0

        self.screen = None
        self.painter = None

        self.point_dict = {}

    def save_point(self, row, index):
        """
        Saves graph coordinates for (row, index) elliptic curve point.
        A point which has been saved one time can't have it's graph coordinates changed afterwards.

        :param row: row of curve point in drawn strategy
        :param index: index of curve point in drawn strategy
        :returns: True if point has been saved this time, False if said point had already been saved and not updated
        """
        if (row, index) in self.point_dict:
            return False
        else:
            self.point_dict.update({(row, index): self.painter.pos()})
            return True

    def restore_point(self, row, index):
        """
        Move drawing coordinates to previously saved (row, index) curve point

        :param row: row of curve point in drawn strategy
        :param index: row of curve point in drawn strategy
        """
        self.painter.penup()
        self.painter.setposition(self.point_dict.get((row, index)))
        self.painter.pendown()

    def init_drawing(self):
        """Initiates screen, turtle and first point"""
        self.screen = turtle.Screen()
        self.screen.screensize()
        self.screen.setup(width=self.screen_width_ratio, height=self.screen_height_ratio)

        self.painter = turtle.Turtle(visible=False)
        self.painter.penup()
        self.painter.goto(0, self.screen.window_height() / 2 - self.turtle_size)
        self.painter.right(90)
        self.painter.pendown()
        self.painter.showturtle()
        self.painter.speed(self.drawing_speed)

        self.painter.write("R0", move=False, align="right", font=("Arial", 16, "bold"))

        self.painter.dot(2 * self.dot_radius, self.dot_color)

    def _init_isogeny(self):
        """Initiates color and branch splitting for isogeny"""
        self.painter.pencolor(self.isogeny_color)
        self.painter.left(self.tree_angle)
        self.number_isogenies = self.number_isogenies + 1

    def _init_doubling(self):
        """Initiates color and branch splitting for isogeny"""
        self.painter.pencolor(self.doubling_color)
        self.painter.right(self.tree_angle)
        self.number_doubling = self.number_doubling + 1

    def _init_arrow(self):
        """Moves outside previous dot before drawing arrow"""
        self.painter.penup()
        self.painter.forward(self.dot_radius)
        self.painter.pendown()

    def _draw_arrow(self):
        """Draws arrow in previously set position, angle and color"""
        self.painter.forward(self.arrow_length)
        arrow_head_origin = self.painter.pos()
        self.painter.left(self.arrow_head_angle)
        self.painter.forward(self.arrow_head_length)
        self.painter.setposition(arrow_head_origin)
        self.painter.right(2 * self.arrow_head_angle)
        self.painter.forward(self.arrow_head_length)
        self.painter.setposition(arrow_head_origin)
        self.painter.left(self.arrow_head_angle)

    def _draw_dot(self):
        """Draws standard dot"""
        self.painter.forward(self.dot_radius)
        self.painter.dot(2 * self.dot_radius, self.dot_color)

    def draw_isogeny(self):
        """Sets correct angle and color then draws isogeny arrow"""
        self._init_isogeny()
        self._init_arrow()
        self._draw_arrow()
        self._draw_dot()
        self.painter.right(self.tree_angle)

    def draw_doubling(self):
        """Sets correct angle and color then draws doubling arrow"""
        self._init_doubling()
        self._init_arrow()
        self._draw_arrow()
        self._draw_dot()
        self.painter.left(self.tree_angle)

    def draw_final_dot(self):
        """Draws dot corresponding to destination curve point"""
        self.painter.dot(2 * self.dot_radius, self.final_dot_color)

    def end_tree(self):
        """Hides turtle drawer at the end"""
        self.painter.hideturtle()

    def save_drawing(self):
        """Saves whole canvas to a file with name set to save_file_name"""
        if self.save_file_name is None:
            now = datetime.datetime.now()
            self.save_file_name = now.strftime("strat_%Y%m%d-%H%M%S.svg")
        canvasvg.saveall(self.save_file_name, self.screen.getcanvas(), margin=50)

    @staticmethod
    def end_drawing():
        """Static method. Ends drawing session"""
        turtle.done()

