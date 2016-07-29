import pygame
import random
from jenna import *
from block import *



pygame.init()
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])
    
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)


clock = pygame.time.Clock()
score = 0
lives = 5

## The scroller object is created here
#any_scroller = Scroller(screen_width, 300, screen_height, (255, 100, 100), 2)

## Font to allow for 
font = pygame.font.SysFont("Gill Sans", 25, True, False)

# Blocks for first run of game, stores them in all the lists
make_blocks()

#check that game is not done
done = False
x_point = 700
city = []

#Start game loop
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True

	
    # Clear the screen
    screen.fill(WHITE)
    color = colors[random.randint(0,5)]
    
    building = Building(color, random.randint(20, 60), random.randint(70, 200), random.randint(0, 800))
    city.append(building)

    for building in city:
        building.draw_building()
        building.move_building()

    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    pos = pygame.mouse.get_pos()
 
    # Fetch the x and y out of the list,
    # just like we'd fetch letters out of a string.
    # Set the player object to the mouse location
    player.rect.x = pos[0]
    player.rect.y = pos[1]

    # See if the player block has collided with anything.
    black_blocks_hit_list = pygame.sprite.spritecollide(player, black_block_list, True)
    green_blocks_hit_list = pygame.sprite.spritecollide(player, green_block_list, True)

    # Move the blocks.
    black_block_list.update()
    green_block_list.update()

    # Check the list of collisions.
    for block in green_blocks_hit_list:
        score += 1

    for block in black_blocks_hit_list:
        lives -= 5

    #Creates the scrote variables using pretty font    
    score_text = font.render("Score: " +str(score), True, BLACK)
    lives_text = font.render("Lives: "+ str(lives), True, BLUE)

    #keeps the text on the page at these coordinates
    screen.blit(score_text, [500, 50])
    screen.blit(lives_text, [50, 50])

    
    # Draw the scrolling background
    #Add your scrolling background here
    #any_scroller.draw_buildings(screen)
    #any_scroller.move_buildings()

    # Draw all the sprites  
    all_sprites_list.draw(screen)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
exit()

