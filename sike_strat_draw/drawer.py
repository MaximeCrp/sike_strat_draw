import turtle
import canvasvg
import datetime


class Drawer:
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
        if (row, index) in self.point_dict:
            print("Already in dict!")
        else:
            self.point_dict.update({(row, index): self.painter.pos()})

    def restore_point(self, row, index):
        self.painter.penup()
        self.painter.setposition(self.point_dict.get((row, index)))
        self.painter.pendown()

    def init_drawing(self):
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

    def init_isogeny(self):
        self.painter.pencolor(self.isogeny_color)
        self.painter.left(self.tree_angle)
        self.number_isogenies = self.number_isogenies + 1

    def init_doubling(self):
        self.painter.pencolor(self.doubling_color)
        self.painter.right(self.tree_angle)
        self.number_doubling = self.number_doubling + 1

    def init_arrow(self):
        self.painter.penup()
        self.painter.forward(self.dot_radius)
        self.painter.pendown()

    def draw_arrow(self):
        self.painter.forward(self.arrow_length)
        arrow_head_origin = self.painter.pos()
        self.painter.left(self.arrow_head_angle)
        self.painter.forward(self.arrow_head_length)
        self.painter.setposition(arrow_head_origin)
        self.painter.right(2 * self.arrow_head_angle)
        self.painter.forward(self.arrow_head_length)
        self.painter.setposition(arrow_head_origin)
        self.painter.left(self.arrow_head_angle)

    def draw_dot(self):
        self.painter.forward(self.dot_radius)
        self.painter.dot(2 * self.dot_radius, self.dot_color)

    def draw_isogeny(self):
        self.init_isogeny()
        self.init_arrow()
        self.draw_arrow()
        self.draw_dot()
        self.painter.right(self.tree_angle)

    def draw_doubling(self):
        self.init_doubling()
        self.init_arrow()
        self.draw_arrow()
        self.draw_dot()
        self.painter.left(self.tree_angle)

    def draw_final_dot(self):
        self.painter.dot(2 * self.dot_radius, self.final_dot_color)

    def end_tree(self):
        self.painter.hideturtle()

    def save_drawing(self):
        if self.save_file_name is None:
            now = datetime.datetime.now()
            self.save_file_name = now.strftime("strat_%Y%m%d-%H%M%S.svg")
        canvasvg.saveall(self.save_file_name, self.screen.getcanvas(), margin=50)

    @staticmethod
    def end_drawing():
        turtle.done()

