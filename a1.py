import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the display surface object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Add Elements Example")

# Define a color (black)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 1. Create a Font object
font = pygame.font.Font(None, 74) # Use default font, size 74

# 2. Create a Text Surface object (the actual image of the text)
text_surface = font.render("Hello, World!", True, WHITE) # Render text in white

# 3. Get a rectangle object for positioning
text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the screen with a background color (e.g., black)
    screen.fill(BLACK)
    
    # 4. Blit (copy) the text surface onto the display surface
    screen.blit(text_surface, text_rect)
    
    # 5. Update the display to make changes visible
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()