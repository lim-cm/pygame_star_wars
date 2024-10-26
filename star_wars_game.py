"""
Michael Lim, Oct 25, 2024
This is a Star Wars themed point and shoot game made in pygame. This is a personal project that I am continuing from an
unfinished project in high school. It was the first project that showed me the joy in coding so I wanted to finish it.
"""
import pygame, sys
from pygame.locals import *
import random, math

#initializing pygame and fps for the game
pygame.init()
FPS = 60
clock = pygame.time.Clock()

#setting up colors
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255, 0, 0)

#screen dimentions/setting up screen w size 1490 x 1000, background color black
SCREEN_WIDTH = 1490
SCREEN_HEIGHT = 1000
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
    for i in range (0, 1500):
        x_pos.append(randomNum(0, SCREEN_WIDTH))
        y_pos.append(randomNum(0, SCREEN_HEIGHT))
        radius.append(randomNum(1,3))
    return x_pos, y_pos, radius

'''
Draws the stars in the background
'''
def draw_stars(x_pos, y_pos, radius):
    for x, y, r in zip(x_pos, y_pos, radius):
        pygame.draw.circle(SCREEN, white, (x, y), r)

def create_crosshairs():
    crosshairs = import_img("image_files/crosshairs.png")  #imports the png for the crosshairs
    scaled_width = crosshairs.get_width() // .7
    scaled_height = crosshairs.get_height() // .7
    scaled_image = pygame.transform.scale(crosshairs, (scaled_width, scaled_height))
    return scaled_image

def create_cockpit():
    cockpit = import_img("image_files/xwing_cockpit.png")  #imports the png for the crosshairs
    scaled_width = cockpit.get_width() // 1.381
    scaled_height = cockpit.get_height() // 1.381
    scaled_image = pygame.transform.scale(cockpit, (scaled_width, scaled_height))
    return scaled_image

def shoot_laser(x, y, dir_x, dir_y, radius):
    x += dir_x * laser_speed
    y += dir_y * laser_speed
    radius -= .15

    # Draw the laser
    pygame.draw.circle(SCREEN, red, (x, y), radius)
    return x,y, radius

'''
The code below and prior to the main game loop initializes important variables
'''
stars_x_pos, stars_y_pos, stars_radii = generateStars()

pygame.mouse.set_visible(False) #TODO: Uncomment when project is done
crosshairs = create_crosshairs()
crosshairs_rect = crosshairs.get_rect()
cockpit = create_cockpit()

laser_radius = 10
laser_speed = 15
lasers1 = []
lasers2 = []
laser_count = 0
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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()       
            laser_count += 1
            # Add laser to list with its direction
            if(laser_count % 2 == 0):
                # Starting position of the lasers at the start of the cockpit, on both sides
                start_x1, start_y1 = 334, 657

                # Calculate direction vector
                dx1 = mouse_x - start_x1
                dy1= mouse_y - start_y1
                
                distance1 = math.sqrt(dx1**2 + dy1**2)
                direction_x1 = dx1 / distance1
                direction_y1 = dy1 / distance1
            
                lasers1.append({
                    "x": start_x1,
                    "y": start_y1,
                    "dir_x": direction_x1,
                    "dir_y": direction_y1,
                    "radius": laser_radius,
                })
                laser_count = 0
            else:
                start_x2, start_y2 = 1072, 657
                dx2 = mouse_x - start_x2
                dy2= mouse_y - start_y2 
                distance2 = math.sqrt(dx2**2 + dy2**2)
                direction_x2 = dx2 / distance2
                direction_y2 = dy2 / distance2
                
                lasers2.append({
                    "x": start_x2,
                    "y": start_y2,
                    "dir_x": direction_x2,
                    "dir_y": direction_y2,
                    "radius": laser_radius,
                })
    
    draw_stars(stars_x_pos, stars_y_pos, stars_radii) #draws stars on the screen
    
    
    #code to display crosshairs
    mouse_x, mouse_y = pygame.mouse.get_pos()
    print(mouse_x, mouse_y)
    crosshairs_rect.center = (mouse_x, mouse_y)
    SCREEN.blit(crosshairs, crosshairs_rect)
    
    # Move and draw each laser
    for laser1 in lasers1:
        if(laser1["radius"] <= 0):
            lasers1.remove(laser1)
        laser1["x"], laser1["y"], laser1["radius"] = shoot_laser(laser1["x"], laser1["y"], laser1["dir_x"], laser1["dir_y"], laser1["radius"])
    
    for laser2 in lasers2:    
        if(laser2["radius"] <= 0):
            lasers2.remove(laser2)
        laser2["x"], laser2["y"], laser2["radius"] = shoot_laser(laser2["x"], laser2["y"], laser2["dir_x"], laser2["dir_y"], laser2["radius"])
    
    
    SCREEN.blit(cockpit, (0,220)) #displays the cockpit 
    pygame.display.update()