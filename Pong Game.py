
import turtle
import time
import pygame


# start game loop
def run_game():


    # draw screen
    screen = turtle.Screen()
    screen.title("Pong")
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.tracer(0)


    # draw paddle 1
    paddle_1 = turtle.Turtle()
    paddle_1.speed(0)
    paddle_1.shape("square")
    paddle_1.color("white")
    paddle_1.shapesize(stretch_wid=5, stretch_len=1)
    paddle_1.penup()
    paddle_1.goto(-350, 0)
    paddle_1.movingUp = False
    paddle_1.movingDown = False
    paddle_1.score = 0

    # draw paddle 2
    paddle_2 = turtle.Turtle()
    paddle_2.speed(0)
    paddle_2.shape("square")
    paddle_2.color("white")
    paddle_2.shapesize(stretch_wid=5, stretch_len=1)
    paddle_2.penup()
    paddle_2.goto(350, 0)
    paddle_2.movingUp = False
    paddle_2.movingDown = False
    paddle_2.score = 0

    # draw ball
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 1
    ball.dy = 1

    # head-up display
    hud = turtle.Turtle()
    hud.speed(0)
    hud.shape("square")
    hud.color("white")
    hud.penup()
    hud.hideturtle()
    hud.goto(0, 260)
    hud.write("0 : 0", align="center", font=("Press Start 2P", 24, "normal"))

    # winner crown
    winner = turtle.Turtle()
    winner.speed(0)
    winner.shape("square")
    winner.color("white")
    winner.penup()
    winner.hideturtle()

    # pause icon
    pause = turtle.Turtle()
    pause.speed(0)
    pause.shape("square")
    pause.color("white")
    pause.penup()
    pause.hideturtle()
    pause.goto(-300, 265)
    pause.write("Space - ⏸️", align="center", font=("Press Start 2P", 18, "normal"))
    pause.status = False

    # victory text
    victory = turtle.Turtle()
    victory.speed(0)
    victory.shape("square")
    victory.color("red")
    victory.penup()
    victory.goto(0, 100)
    victory.hideturtle()

    # background up line
    up_line = turtle.Turtle()
    up_line.speed(0)
    up_line.shape("square")
    up_line.color("white")
    up_line.penup()
    up_line.goto(0, 250)
    up_line.shapesize(stretch_wid=0.5, stretch_len=40)

    # background middle lines
    middle_lines = []

    for i in range(10):
        middle_lines.append(turtle.Turtle())
        middle_lines[i].speed(0)
        middle_lines[i].shape("square")
        middle_lines[i].color("white")
        middle_lines[i].penup()
        middle_lines[i].goto(0, 212 - (i*55))
        middle_lines[i].shapesize(stretch_wid=2, stretch_len=0.5)


    # starting the game method
    def start_game():
        ball_movement()

    
    # clear and reset game method
    def clear_game():
        screen.clearscreen()
        run_game()


    # play soundtracks
    def play_soundtrack():
        soundtrack_2 = pygame.mixer.music.load('megalovania.ogg')
        pygame.mixer.music.play()


    # play interaction sounds
    def play_sound_interaction(sound):
        interaction = pygame.mixer.Sound(sound)
        interaction.play()

    # ball movement method
    def ball_movement():
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)


    def paddle_1_up():
        y = paddle_1.ycor()

        if paddle_1.movingUp:

            if y < 190:
                y += 1

        paddle_1.sety(y)


    def paddle_1_set_moving_up_true():
        paddle_1.movingUp = True


    def paddle_1_set_moving_up_false():
        paddle_1.movingUp = False


    def paddle_1_down():
        y = paddle_1.ycor()

        if paddle_1.movingDown:

            if y > -250:
                y -= 1

        paddle_1.sety(y)


    def paddle_1_set_moving_down_true():
        paddle_1.movingDown = True


    def paddle_1_set_moving_down_false():
        paddle_1.movingDown = False


    def paddle_2_up():
        y = paddle_2.ycor()

        if paddle_2.movingUp:

            if y < 190:
                y += 1

        paddle_2.sety(y)


    def paddle_2_set_moving_up_true():
        paddle_2.movingUp = True


    def paddle_2_set_moving_up_false():
        paddle_2.movingUp = False


    def paddle_2_down():
        y = paddle_2.ycor()

        if paddle_2.movingDown:

            if y > -250:
                y -= 1

        paddle_2.sety(y)


    def paddle_2_set_moving_down_true():
        paddle_2.movingDown = True


    def paddle_2_set_moving_down_false():
        paddle_2.movingDown = False

    # function to pause the game
    def pause_game():
        pause.status = not pause.status
        pause.clear()

        if pause.status:
            pause.write("Space - ⏯️", align="center", font=("Press Start 2P", 18, "normal"))
            play_sound_interaction("pause_on.wav")
            pygame.mixer.music.pause()

        else:
            pause.write("Space - ⏸️", align="center", font=("Press Start 2P", 18, "normal"))
            play_sound_interaction("pause_off.wav")
            pygame.mixer.music.unpause()


    # function of test the win condition
    def win_condition():
        if paddle_1.score == 5:
            victory.write("Player 1 Wins. Continue? y -> Yes n -> No ", align="center", font=("Press Start 2P", 25, "normal"))
            pause.status = not pause.status
            pygame.mixer.music.pause()
            play_sound_interaction("victory_sound.wav")

            screen.onkeypress(clear_game, "y")
            screen.onkeypress(screen.bye, "n")
            
        elif paddle_2.score == 5:
            victory.write("Player 2 Wins. Continue? y -> Yes n -> No ", align="center", font=("Press Start 2P", 25, "normal"))

            pause.status = not pause.status
            pygame.mixer.music.pause()
            play_sound_interaction("victory_sound.wav")

            screen.onkeypress(clear_game, "y")
            screen.onkeypress(screen.bye, "n")


    # keyboard
    screen.listen()
    screen.onkeypress(paddle_1_set_moving_up_true, "w")
    screen.onkeypress(paddle_1_set_moving_down_true, "s")
    screen.onkeyrelease(paddle_1_set_moving_up_false, "w")
    screen.onkeyrelease(paddle_1_set_moving_down_false, "s")


    screen.onkeypress(paddle_2_set_moving_up_true, "Up")
    screen.onkeypress(paddle_2_set_moving_down_true, "Down")
    screen.onkeyrelease(paddle_2_set_moving_up_false, "Up")
    screen.onkeyrelease(paddle_2_set_moving_down_false, "Down")


    # timer before the game starts
    def timer():
        timer = turtle.Turtle()
        timer.speed(0)
        timer.shape("square")
        timer.color("white")
        timer.penup()
        timer.hideturtle()
        timer.goto(0, 0)

        
        pygame.init()
        play_sound_interaction("simple_game_countdown.wav")
        timer.clear()
        timer.write("3", align="center", font=("Press Start 2P", 40, "normal"))
        time.sleep(1)
        timer.clear()
        timer.write("2", align="center", font=("Press Start 2P", 40, "normal"))
        time.sleep(1)
        timer.clear()
        timer.write("1", align="center", font=("Press Start 2P", 40, "normal"))
        time.sleep(1)
        timer.clear()
        timer.write("Go!", align="center", font=("Press Start 2P", 40, "normal"))
        time.sleep(1)
        timer.clear()

        # enable pause
        screen.onkeypress(pause_game, " ")


    # change crown position
    def new_score():
        winner.clear()

        if paddle_1.score < paddle_2.score:
            winner.goto(100, 265)
            winner.write("👑", align="center", font=("Press Start 2P", 24, "normal"))
        elif paddle_1.score > paddle_2.score:
            winner.goto(-100, 265)
            winner.write("👑", align="center", font=("Press Start 2P", 24, "normal"))


    # render game
    def render():
        screen.update()

        if not pause.status:
            # paddles movement
            paddle_1_up()
            paddle_1_down()
            paddle_2_up()
            paddle_2_down()

            # collision with the upper wall
            if ball.ycor() > 240:
                ball.sety(240)
                ball.dy *= -1
                play_sound_interaction("hit_wall.wav")

            # collision with lower wall
            if ball.ycor() < -280:
                ball.sety(-280)
                ball.dy *= -1
                play_sound_interaction("hit_wall.wav")

            # collision with paddle_1
            if ball.xcor() == -335 and paddle_1.ycor() + 75 > ball.ycor() > paddle_1.ycor() - 75:
                ball.dx = 1
                play_sound_interaction("hit_paddle.wav")

            # Critic Strike with paddle_1
            if ball.xcor() == -325 and paddle_1.ycor() + 25 > ball.ycor() > paddle_1.ycor() - 25:
                ball.dx = 3
                play_sound_interaction("critic_hit.wav")

            # collision with paddle_2
            if ball.xcor() == 335 and paddle_2.ycor() + 75 > ball.ycor() > paddle_2.ycor() - 75:
                ball.dx = -1
                play_sound_interaction("hit_paddle.wav")

            # Critic Strike with paddle_2
            if ball.xcor() == 325 and paddle_2.ycor() + 25 > ball.ycor() > paddle_2.ycor() - 25:
                ball.dx = -3
                play_sound_interaction("critic_hit.wav")

            # collision with left wall
            if ball.xcor() < -375:
                ball.color("red")
                paddle_2.score += 1
                hud.clear()
                hud.write("{} : {}" .format(paddle_1.score, paddle_2.score),
                        align="center", font=("Press Start 2p", 24, "normal"))
                
                play_sound_interaction("score_up_sound.wav")
                win_condition()

                # Pause before game restarts          
                screen.update()
                time.sleep(1)
                ball.color("white")

                ball.goto(0, 0)
                ball.dx = 1
                ball.dx *= -1
                ball.dy *= -1

                new_score()

            # collision with right wall
            if ball.xcor() > 375:
                ball.color("red")
                paddle_1.score += 1
                hud.clear()
                hud.write("{} : {}" .format(paddle_1.score, paddle_2.score),
                        align="center", font=("Press Start 2p", 24, "normal"))
                
                play_sound_interaction("score_up_sound.wav")
                win_condition()
                
                # Pause before game restarts          
                screen.update()
                time.sleep(1)
                ball.color("white")

                ball.goto(0, 0)
                ball.dx = -1
                ball.dx *= -1
                ball.dy *= -1

                new_score()
            
            # ball movement
            start_game()
    

    timer()

    play_soundtrack()

    while True:
        render()

run_game()