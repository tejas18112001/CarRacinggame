import pygame
import time
import random
pygame.init()
grey = (119, 118, 110)
display_width = 800
display_height = 600
game_screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
car_img = pygame.image.load('car.png')      # CAR.PNG
backgroundpic = pygame.image.load("bbb.png")
#backdroundpic = pygame.transform.scale(backgroundpic, (400, 400))
car_width = 56
black = (0, 0, 0)

def obstacle(obs_startx,obs_starty,obs):
     global obs_pic                             #****************
     if obs == 0:
        obs_pic = pygame.image.load("enemy_car_1.png")

     elif obs == 1:
        obs_pic = pygame.image.load("enemy_car_2.png")

     elif obs == 2:
         obs_pic = pygame.image.load("car.png")


     elif obs == 3:
         obs_pic = pygame.image.load("car6.png")

     game_screen.blit( obs_pic ,(obs_startx , obs_starty ))       # game_screen.blit( obs_pic ,(obs_startx , obs_starty ))

def text_object(text, font):
    textsurface = font.render(text, True, black)
    return textsurface, textsurface.get_rect()


def message_display(text):
    largetext = pygame.font.Font("freesansbold.ttf", 80)
    textsurf, textrect = text_object(text, largetext)
    textrect.center = (400, 300)
    game_screen.blit(textsurf, textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()


def crash():
    message_display("YOU CRASHED")


def car(x, y):
    game_screen.blit(car_img, (x, y))


def background():
    game_screen.blit(backgroundpic, (0, 0))


def game_loop():
    global event
    x = (display_width * 0.45)
    y = (display_height * 0.82)
    x_change = 0
    obstacle_speed =9
    obs=0
    y_change=0
    obs_startx = random.randrange(650, 670)    #  obs_startx = random.randrange(350, (display_width - 450)
    obs_starty = -750           # ****************
    obs_width = 50
    obs_height = 100
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

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

        x += x_change

        game_screen.fill(grey)
        background()
        obs_starty -= (obstacle_speed/4)
       # obs_starty += obstacle_speed            # this y reported every time
        obstacle(obs_startx , obs_starty , obs)
        obs_starty += obstacle_speed
        car(x, y)


        if x < 220 or x > 450:
            crash()
            bumped = True
        if x> display_width -(car_width + 110 ) or x<110:
            crash()
        if obs_starty> display_height:
            obs_starty = 0 - obs_height
            obs_startx = random.randrange(170 , ( display_width - 170))
            obs = random.randrange(0 , 4)

            if y< obs_starty + obs_height:
                if x > obs_startx and x < obs_startx + obs_width :
                    crash()
        #***************
        pygame.display.update()

        clock.tick(60)




game_loop()
pygame.quit()
quit()