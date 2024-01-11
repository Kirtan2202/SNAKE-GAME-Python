from turtle import Turtle, Screen

STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_FORWARD = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    
    def __init__(self):
        self.segment_list = []
        self.createSnake()
        self.head = self.segment_list[0]
             
    def createSnake(self):
        for segments_position in STARTING_POSITION:
            self.add_segments(segments_position)
            
            
    def add_segments(self, position):
        snake = Turtle()
        snake.shape("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.segment_list.append(snake)
            
    
    def extend(self):
        self.add_segments(self.segment_list[-1].position())
    

    def move(self):
        for snk in range((len(self.segment_list)-1),0,-1):  #start, end, step, range fn is c++ so we cannot write this - range(start=2, end=0, step=-1)
            new_x = self.segment_list[snk-1].xcor()
            new_y = self.segment_list[snk-1].ycor()
            self.segment_list[snk].goto(new_x, new_y)
        self.segment_list[0].forward(MOVE_FORWARD)
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        