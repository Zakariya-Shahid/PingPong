import stddraw
import stdio
import math
import random

paddle_width = 0.030
paddle_height = 0.35
paddle1_x = 0.2
paddle1_y = 0.3
paddle2_x = 0.8
paddle2_y = 0.3
ball_radius = 0.010
ball_x = 0.5
ball_y = 0.5

# function to draw paddles of ping pong game
def pong_paddle(y1,y2):
    stddraw.clear()
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.filledRectangle(paddle1_x, paddle1_y, paddle_width, paddle_height)
    stddraw.filledRectangle(paddle2_x, paddle2_y, paddle_width, paddle_height)

    stddraw.setPenColor(stddraw.BLACK)
    stddraw.filledCircle(ball_x, ball_y, ball_radius)



def pong_boundaries():
    pass

def pong_input():
    global paddle1_y, paddle2_y
    # configuring the w and s keys to move up and down the paddle 1
    if stddraw.hasNextKeyTyped():
        key = stddraw.nextKeyTyped()
        if key == 'w':
            print("Move the paddle 1 up")
        if key == 's':
            print("Move the paddle 1 down")

            # configuring the i and k keys to move up and down the paddle 2
        if key == 'i':
            print("Move the paddle 2 up")
        if key == 'k':
            print("Move the paddle 2 down")



def main():
    while True:
        pong_paddle(paddle1_y, paddle2_y)
        pong_input()
        stddraw.show(10)


if __name__ == '__main__':
    main()