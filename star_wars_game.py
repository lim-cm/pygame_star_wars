"""
Michael Lim, Oct 25, 2024
This is a Star Wars themed point and shoot game made in pygame. This is a personal project that I am continuing from an
unfinished project in high school. It was the first project that showed me the joy in coding so I wanted to finish it.
"""
import pygame, sys
from pygame.locals import *
import random

#initializing pygame and fps for the game
pygame.init()
FPS = 60
clock = pygame.time.Clock()

#setting up colors
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)

#screen dimentions/setting up screen w size 300x300, background color black
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 780
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
SCREEN.fill(black)
pygame.display.set_caption("Star Wars Game")

def import_img(image_path):
    return pygame.image.load(image_path)

'''
Generates a random integer in a range
'''
def randomNum(start, end):
    return random.randrange(start, end)

'''
Generates Stars in the background
'''
def generateStars():
    x_pos = []
    y_pos = []
    radius = []
    for i in range (0, 1000):
        x_pos.append(randomNum(0, 1200))
        y_pos.append(randomNum(0, 780))
        radius.append(randomNum(1,3))
    return x_pos, y_pos, radius

'''
Draws the stars in the background
'''
def draw_stars(x_pos, y_pos, radius):
    for x, y, r in zip(x_pos, y_pos, radius):
        pygame.draw.circle(SCREEN, white, (x, y), r)

def create_crosshairs():
    crosshairs = import_img("pngfiles/crosshairs2.png")  #imports the png for the crosshairs
    scaled_width = crosshairs.get_width() // 1.2
    scaled_height = crosshairs.get_height() // 1.2
    scaled_image = pygame.transform.scale(crosshairs, (scaled_width, scaled_height))
    
    return scaled_image

'''
The code below and prior to the main game loop initializes important variables
'''
stars_x_pos, stars_y_pos, stars_radii = generateStars()

#pygame.mouse.set_visible(False) TODO: Uncomment when project is done
crosshairs = create_crosshairs()
crosshairs_rect = crosshairs.get_rect()
"""
Main game loop
"""
while True:
    SCREEN.fill(black) #fill screen with color to get rid of last frame
    clock.tick(FPS) #limits FPS to 60
    for event in pygame.event.get():
        # if statement to quit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    draw_stars(stars_x_pos, stars_y_pos, stars_radii) #draws stars on the screen
    
    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    crosshairs_rect.center = (mouse_x, mouse_y)
    SCREEN.blit(crosshairs, crosshairs_rect)
    
    

    pygame.display.update()