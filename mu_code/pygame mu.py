import pygame

# Initialize Pygame
pygame.init()

# Set the screen dimensions
screen_width = 1820
screen_height = 980
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mountain Climber")
background_color = (133, 225, 245)

# Load your sprite image
player_image = pygame.image.load('sprites/player.png')
block_image = pygame.image.load('sprites/grass_block.png')
icon_image = pygame.image.load('sprites/game_icon.jpg')
pygame.display.set_icon(icon_image)

# Set the initial position and velocity of the sprite
player_x = 0
player_y = 800
player_vel_y = 0
player_speed = 8
gravity = 0.5
jump_vel = -15

block_x = 1000
block_y = 932

# Game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_vel_y = jump_vel

def update():
    global player_y, player_vel_y

    # Handle player movement
    player_vel_y += gravity
    player_y += player_vel_y
    if player_y > screen_height - player_image.get_height():
        player_y = screen_height - player_image.get_height()
        player_vel_y = 0

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_d]:
        player_x += player_speed

    # Handle collision between player and block
    player_rect = pygame.Rect(
        player_x, player_y, player_image.get_width(), player_image.get_height()
        )

    block_rect = pygame.Rect(
        block_x, block_y, block_image.get_width(), block_image.get_height())

    if player_rect.colliderect(block_rect):
        # Collision detected, reset player position and momentum
        player_y = screen_height - player_image.get_height()
        player_vel_y = 0

    # Set the background color
    screen.fill(background_color)

    # Add gravity to how fast player is falling
    player_vel_y += gravity

    # Move player based off how fast player is falling
    player_y += player_vel_y

    # Keep player in screen borders
    if player_y > screen_height - player_image.get_height():
        player_y = screen_height - player_image.get_height()
        player_vel_y = 0
    if player_y < 0:
        player_y = screen_height - player_image.get_height()
        player_y = 0
    if player_x > 1774:
        player_x = screen_width - player_image.get_width()
        player_x = 1774
    if player_x < 0:
        player_x = screen_width - player_image.get_width()
        player_x = 0

    # Draw sprites
    screen.blit(player_image, (player_x, player_y))
    screen.blit(block_image, (block_x, block_y))

    pygame.display.update()
pygame.quit()