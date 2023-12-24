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
def pong_paddle():
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.filledRectangle(paddle1_x, paddle1_y, paddle_width, paddle_height)
    stddraw.filledRectangle(paddle2_x, paddle2_y, paddle_width, paddle_height)

    stddraw.setPenColor(stddraw.BLACK)
    stddraw.filledCircle(ball_x, ball_y, ball_radius)



def pong_boundaries():
    pass

def pong_input():
    pass


def main():
    while True:
        pong_paddle()
        # pong_boundaries()
        # pong_input()
        stddraw.show(10)


if __name__ == '__main__':
    main()