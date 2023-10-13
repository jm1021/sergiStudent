import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Frog Obstacle Course")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)

# Load frog images and facts
frog_images = [pygame.image.load(f'frog{i}.png') for i in range(1, 7)]
frog_facts = [
    "Frogs are amphibians.",
    "Some frogs can jump 20 times their body length.",
    "Frogs don't drink water; they absorb it through their skin.",
    "A group of frogs is called an army.",
    "The wood frog can survive being frozen.",
    "The golden poison dart frog is one of the most toxic animals."
]

# Game loop
selected_frog = None
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            selected_frog = random.choice(range(1, 7))

    # Draw background
    screen.fill(white)

    # Display frog images and facts
    for i in range(1, 7):
        x = i * 100
        screen.blit(frog_images[i - 1], (x, height // 2 - 50))
        if selected_frog == i:
            fact_font = pygame.font.Font(None, 24)
            fact_text = fact_font.render(frog_facts[i - 1], True, black)
            screen.blit(fact_text, (width // 2 - 150, height // 2 + 50))

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(30)
