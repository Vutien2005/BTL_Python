import pygame

pygame.init()

# Set up the window

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Black Myth Wukong")

# Define colors

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


player_x = 300
player_y = 450
player_width = 64
player_height = 64
player_vel = 5



running = True

while running:
    screen.fill(white)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    pygame.display.update()

pygame.quit()
