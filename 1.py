# import pygame
# import sys
#
# pygame.init()
#
# screen_width = 800
# screen_height = 600
# game_display = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("MY GAME")
# grey = (119, 118, 110)
#
# bumped = True
# while bumped:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#
#     game_display.fill(grey)
#     pygame.display.update()
#
#
# def pause():              # at the top loop in main function rememberedd
#     pause = False
#     while pause:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#                 sys.exit()
#         game_screen.blit(instruction_background, (0, 0))
#
#         smalltext = pygame.font.Font("freesansbold.ttf", 100)
#
#         textsurf, textrect = text_object("PAUSED", smalltext)
#         textrect.center = (400, 200)
#         game_screen.blit(textsurf, textrect)
#
#         button("CONTINUE", 100, 520, 150, 50, purple, bright_purple, "continue")
#         button("RESTART", 550, 520, 130, 50, red, bright_red, "restart")
#         button("MAIN MENU", 300, 520, 200, 50, blue, bright_blue, "main menu")
#
#         pygame.display.update()
#         clock.tick(50)




# also import music using same
import sys
#from typing import Union

import pygame
import time         # we have to sleep event for some time
import random       # for random entry of cars
#import vlc

from pygame.surface import SurfaceType, Surface

pygame.init()
grey = (119, 118, 110)
display_width = 800
display_height = 600
game_screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
car_img = pygame.image.load('carB345.jpg')  # car.png
# backgroundpic = pygame.image.load("bbb.png")
# backdroundpic = pygame.transform.scale(backgroundpic, (400, 400))
car_width = 56
black = (0, 0, 0)
white= (255,255,255)
grass = pygame.image.load("grass.jpg")  #
strip = pygame.image.load("strip.jpg")
yellow_strip = pygame.image.load("yellow_strip.jpg")
intro_background = pygame.image.load("bac1.jpg")
instruction_background = pygame.image.load("back123.jpg")
tree = pygame.image.load("tree1.png")
red = (200, 0, 0)
bright_red = (255, 0, 0)

blue = (0, 0, 200)
bright_blue = (0, 0, 255)

purple = (207, 3, 252)
bright_purple = (186, 3, 252)

pygame.mixer.init()
pygame.mixer.music.load("MoneyHeist.mp3")
pygame.mixer.music.play(loops=-1)



def horn():
    paused = False
    while not paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()


        pygame.mixer.music.load("mixkit-car-horn-718.mp3")
        pygame.mixer.music.play()


def intro_loop():

    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        game_screen.blit(intro_background, (0, 0))

        # largetext = pygame.font.Font("freesansbold.ttf", 115)
        largetext = pygame.font.Font("freesansbold.ttf", 50)

        textsurf, textrect = text_object(" WELCOME TO CAR GAME", largetext)
        textrect.center = (400, 80)
        game_screen.blit(textsurf, textrect)
        button("START", 150, 520, 100, 50, purple, bright_purple, "play")
        button("QUIT", 550, 520, 100, 50, red, bright_red, "quit")
        button("INSTRUCTION", 300, 520, 200, 50, blue, bright_blue, "intro")


        pygame.display.update()
        clock.tick(50)


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:  # if x + w > mouse[0] > x and not y + h <= mouse[1] > y:

        pygame.draw.rect(game_screen, ac, (x, y, w, h))

        smalltext = pygame.font.Font("freesansbold.ttf", 20)
        textsurf, textrect = text_object(msg, smalltext)
        textrect.center = ((x + (w / 2)), (y + (h / 2)))
        game_screen.blit(textsurf, textrect)

        if click[0] == 1 and action != None:
            if action == "play":
                game_loop()
            elif action == "quit":
                pygame.quit()
                quit()
            elif action == "intro":

                introduction()

            elif action == "menu":
                intro_loop()
            elif action == "continue":
                game_loop()

            elif action == "main menu":
                introduction()
            elif action == "Restart":  # *********************************************************************
                game_loop()


    else:
        pygame.draw.rect(game_screen, ic, (x, y, w, h))
        smalltext = pygame.font.Font("freesansbold.ttf", 20)
        textsurf, textrect = text_object(msg, smalltext)
        textrect.center = ((x + (w / 2)), (y + (h / 2)))
        game_screen.blit(textsurf, textrect)


def introduction():

    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        game_screen.blit(instruction_background, (0, 0))

        largetext = pygame.font.Font("freesansbold.ttf", 80)
        smalltext = pygame.font.Font("freesansbold.ttf", 20)
        mediumtext = pygame.font.SysFont("freesansbold.ttf", 40)



        Textsurf, Textrect = text_object(" This is The Car Game in Which You Have To Dodge The Comming Cars", smalltext)
        Textrect.center = (400, 200)

        textsurf, textrect = text_object(" INSTRUCTION", largetext)
        textrect.center = (400, 100)

        game_screen.blit(Textsurf, Textrect)
        game_screen.blit(textsurf, textrect)

        ltextsurf, ltextrect = text_object("ARROW LEFT : LEFT TURN  ", smalltext)
        ltextrect.center = (150, 400)
        rtextsurf, rtextrect = text_object("ARROW RIGHT :  RIGHT TURN ", smalltext)
        rtextrect.center = (150, 450)
        atextsurf, atextrect = text_object("A : ACCELERATOR  ", smalltext)
        atextrect.center = (150, 500)

        btextsurf, btextrect = text_object("B: BRAKE  ", smalltext)
        btextrect.center = (150, 550)

        ptextsurf, ptextrect = text_object("P : PAUSE  ", smalltext)
        ptextrect.center = (150, 350)

        ctextsurf, ctextrect = text_object("CONTROL  ", mediumtext)
        ctextrect.center = (150, 300)

        game_screen.blit(ltextsurf, ltextrect)
        game_screen.blit(rtextsurf, rtextrect)
        game_screen.blit(atextsurf, atextrect)
        game_screen.blit(btextsurf, btextrect)
        game_screen.blit(ptextsurf, ptextrect)
        game_screen.blit(ctextsurf, ctextrect)

        button("BACK", 600, 450, 100, 50, red, bright_red, "menu")

        # button("Back to pause page" , 550 ,510 ,200 ,50 ,red , bright_red , "paused2")
        pygame.display.update()
        clock.tick(30)


def obstacle(obs_startx, obs_starty, obs):
    global obs_pic  # ****************
    if obs == 0:
        obs_pic = pygame.image.load("enemy_car_1.png")

    elif obs == 1:
        obs_pic = pygame.image.load("enemy_car_2.png")

    elif obs == 2:
        obs_pic = pygame.image.load("car.png")


    elif obs == 3:
        obs_pic = pygame.image.load("car6.png")

    game_screen.blit(obs_pic, (obs_startx, obs_starty))  # game_screen.blit( obs_pic ,(obs_startx , obs_starty ))


def score_system(passed, score, level):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Passed = " + str(passed), True, black)
    score = font.render("Score= " + str(score), True, red)
    level = font.render("Level = " + str(level), True, bright_blue)

    pygame.mixer.music.load("level.mp3")
    pygame.mixer.music.play()

    game_screen.blit(text, (0, 50))
    game_screen.blit(score, (0, 30))
    game_screen.blit(level, (0, 70))


def text_object(text, font):
    textsurface = font.render(text, True, black)
    return textsurface, textsurface.get_rect()


def message_display(text):
    largetext = pygame.font.Font("freesansbold.ttf", 80)

    textsurf, textrect = text_object(text, largetext)
    textrect.center = (400, 300)
    game_screen.blit(textsurf, textrect)
    pygame.display.update()
    time.sleep(2)
    game_loop()


def crash():
    message_display("YOU CRASHED")


def car(x, y):
    game_screen.blit(car_img, (x, y))


def background():
    game_screen.blit(grass, (0, 0))
    game_screen.blit(grass, (700, 0))
    game_screen.blit(yellow_strip, (400, 0))
    game_screen.blit(yellow_strip, (400, 100))
    game_screen.blit(yellow_strip, (400, 200))
    game_screen.blit(yellow_strip, (400, 300))
    game_screen.blit(yellow_strip, (400, 400))
    game_screen.blit(yellow_strip, (400, 500))
    game_screen.blit(yellow_strip, (400, 600))
    game_screen.blit(strip, (120, 0))
    game_screen.blit(strip, (680, 0))
    game_screen.blit(tree, (50,30))



def game_loop():
    global event
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    obstacle_speed = 8
    obs = 0
    y_change = 0
    obs_startx = random.randrange(200,(display_height - 200))  # obs_startx = random.randrange(350, (display_width - 450)
    obs_starty = -750  # ****************
    obs_width = 50
    obs_height = 100
    # ****************************
    passed = 0
    level = 0
    score = 0
    y2 = 0


    bumped = False
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5

                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_a:
                    obstacle_speed += 2
                if event.key == pygame.K_b:
                    obstacle_speed -= 2

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        game_screen.fill(grey)

        rel_y = y2 % grass.get_rect().width

        game_screen.blit(grass, (0, rel_y - grass.get_rect().width))

        game_screen.blit(grass ,(700, rel_y - grass.get_rect().width))
        if rel_y < 800:

            game_screen.blit(grass, (0, rel_y))
            game_screen.blit(grass, (700, rel_y))
            game_screen.blit(yellow_strip, (400, rel_y))
            game_screen.blit(yellow_strip, (400, rel_y + 100))
            game_screen.blit(yellow_strip, (400, rel_y + 200))
            game_screen.blit(yellow_strip, (400, rel_y + 300))
            game_screen.blit(yellow_strip, (400, rel_y + 400))
            game_screen.blit(yellow_strip, (400, rel_y + 500))
            game_screen.blit(yellow_strip, (400, rel_y - 100))
            game_screen.blit(strip, (120, rel_y - 200))
            game_screen.blit(strip, (120, rel_y + 20))
            game_screen.blit(strip, (120, rel_y + 30))
            game_screen.blit(strip, (680, rel_y - 100))
            game_screen.blit(strip, (680, rel_y + 20))
            game_screen.blit(strip, (680, rel_y + 30))

           # game_screen.blit(tree, (30, rel_y + 30))
           # game_screen.blit(tree, (30, rel_y + 200))
           # game_screen.blit(tree, (30, rel_y + 370))

           # game_screen.blit(tree, (720, rel_y + 30))
           # game_screen.blit(tree, (720, rel_y + 200))
          #  game_screen.blit(tree, (720, rel_y + 370))

            #game_screen.blit(tree, (30, rel_y + 120))

        y2  +=obstacle_speed

        #background()
        obs_starty -= (obstacle_speed / 4)
        # obs_starty += obstacle_speed            # this y reported every time
        obstacle(obs_startx, obs_starty, obs)
        obs_starty += obstacle_speed
        car(x, y)
        score_system(passed, score, level)
        # **********************************************************************
        # pygame.display.update()
        #button("HORN" , 650 ,50 ,100 ,50 ,red , bright_red , "horn")

        if x > 690 - car_width or x < 110:  # when car touch boundry
            pygame.mixer.init()
            pygame.mixer.music.load("car_crash.mp3")
            pygame.mixer.music.play()
            crash()

        # if x> display_width -(car_width + 110 ) or x<110:
        # crash()
        if obs_starty > display_height:
            obs_starty = 0 - obs_height
            obs_startx = random.randrange(170, (display_width - 170))
            obs = random.randrange(0, 4)
            passed = passed + 1
            score = passed * 10
            if int(passed) % 10 == 0:
                level = level + 1
                obstacle_speed = obstacle_speed + 2
                largetext = pygame.font.Font("freesansbold.ttf", 100)
                textsurf, textrect = text_object("level " + str(level), largetext)
                textrect.center = (400, 300)
                game_screen.blit(textsurf, textrect)
                pygame.display.update()
                time.sleep(2)
        # if y < ( obs_starty + obs_height ) :

        if y < (obs_starty + obs_height):

            if x > obs_startx and x < obs_startx + obs_width or x + car_width > obs_startx and x + car_width < obs_startx + obs_width:
                pygame.mixer.init()
                pygame.mixer.music.load("car_crash.mp3")
                pygame.mixer.music.play()
                crash()

        button("PAUSED", 600, 600, 100, 50, blue, bright_blue, "pause")



        pygame.display.update()

        clock.tick(60)


# pause_loop()
intro_loop()
game_loop()
pygame.quit()
quit()
pygame.mixer.unload()
