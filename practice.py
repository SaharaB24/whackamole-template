import pygame
import random

# Initialize Pygame
pygame.init()

# Set up screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Random Image Movement')

# Load the image
image = pygame.image.load('your_image.png')  # Replace with your image path
image_rect = image.get_rect()

# Set initial position of the image
image_rect.topleft = (WIDTH // 2, HEIGHT // 2)

# Colors
WHITE = (255, 255, 255)

# Set up the clock for framerate control
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse click is on the image
            if image_rect.collidepoint(event.pos):
                # Move the image to a random position
                new_x = random.randint(0, WIDTH - image_rect.width)
                new_y = random.randint(0, HEIGHT - image_rect.height)
                image_rect.topleft = (new_x, new_y)

    # Fill the screen with a white background
    screen.fill(WHITE)

    # Draw the image at the new position
    screen.blit(image, image_rect)

    # Update the screen
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
