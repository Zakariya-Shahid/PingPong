import stddraw
import stdio
import time
import random

paddle_width = 0.030
paddle_height = 0.35
paddle1_x = 0.1
paddle1_y = 0.3
paddle2_x = 0.9
paddle2_y = 0.3
ball_radius = 0.010
ball_x = 0.5
ball_y = 0.5

# generating two random float number between 0 to 0.2 and assigning them to velocity_x and velocity_y
velocity_x = random.uniform(0.0015, 0.004)
velocity_y = random.uniform(0.0015, 0.004)

# function to draw paddles of ping pong game
def pong_paddle(y1,y2):
    stddraw.clear()
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.filledRectangle(paddle1_x, paddle1_y, paddle_width, paddle_height)
    stddraw.filledRectangle(paddle2_x, paddle2_y, paddle_width, paddle_height)

    stddraw.setPenColor(stddraw.BLACK)
    stddraw.filledCircle(ball_x, ball_y, ball_radius)

def pong_input():
    global paddle1_y, paddle2_y
    # configuring the w and s keys to move up and down the paddle 1
    if stddraw.hasNextKeyTyped():
        key = stddraw.nextKeyTyped()
        if key == 'w':
            paddle1_y += 0.1
        if key == 's':
            paddle1_y -= 0.1

            # configuring the i and k keys to move up and down the paddle 2
        if key == 'i':
            paddle2_y += 0.1
        if key == 'k':
            paddle2_y -= 0.1

def move_ball():
    global ball_x, ball_y, velocity_x, velocity_y


    if ball_x >= 1:
        print("Player 1 wins")
        # ending program
        time.sleep(3)
        exit()
    if ball_x <= 0:
        print("Player 2 wins")
        # ending program
        time.sleep(3)
        exit()
    if ball_y >= 1:
        velocity_y = -velocity_y
    if ball_y <= 0:
        velocity_y = -velocity_y

    ball_x += velocity_x
    ball_y += velocity_y



def main():
    while True:
        pong_paddle(paddle1_y, paddle2_y)
        move_ball()
        pong_input()
        stddraw.show(10)


if __name__ == '__main__':
    main()