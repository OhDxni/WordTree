import pygame
import sys


pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Tree with Buttons')

# Define colors
WHITE = (255, 255, 255)
BROWN = (101, 67, 33)
GREEN = (34, 139, 34)
DARK_GREEN = (0, 100, 0)
GRASS_GREEN = (0, 128, 0)
RED = (255, 0, 0)
DARK_RED = (200, 0, 0)
SKY_BLUE = (135, 206, 250)
CLOUD_COLOR = (255, 255, 255)

# Define button properties
button_color = RED
button_hover_color = DARK_RED
button_text_color = (255, 255, 255)

# Font for button text
font_very_small = pygame.font.SysFont('Arial', 12)
font_small = pygame.font.SysFont('Arial', 16)
font_default = pygame.font.SysFont('Arial', 20)


# Button class to handle drawing and interaction
class Button:
    def __init__(self, x, y, radius, text, font):
        self.x = x
        self.y = y
        self.radius = radius
        self.text = text
        self.font = font
        self.clicked = False

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        color = button_hover_color if self.is_hovered(mouse_pos) else button_color
        pygame.draw.circle(screen, color, (self.x, self.y), self.radius)

        text_surface = self.font.render(self.text, True, button_text_color)
        text_rect = text_surface.get_rect(center=(self.x, self.y))
        screen.blit(text_surface, text_rect)

    def is_hovered(self, mouse_pos):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, 2 * self.radius, 2 * self.radius).collidepoint(
            mouse_pos)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_hovered(event.pos):
                self.clicked = True
                return True
        return False


# Function to draw the tree
def draw_tree(screen):
    # Draw the trunk with shading for a 3D effect
    pygame.draw.rect(screen, BROWN, (390, 350, 20, 200))  # Center trunk
    pygame.draw.rect(screen, (80, 50, 30), (400, 350, 10, 200))  # Darker side for depth

    # Draw branches, more spaced out
    pygame.draw.line(screen, BROWN, (400, 350), (150, 300), 15)  # Leftmost branch
    pygame.draw.line(screen, BROWN, (400, 350), (650, 300), 15)  # Rightmost branch
    pygame.draw.line(screen, BROWN, (400, 300), (220, 230), 10)  # Middle-left branch
    pygame.draw.line(screen, BROWN, (400, 300), (580, 230), 10)  # Middle-right branch
    pygame.draw.line(screen, BROWN, (400, 270), (400, 170), 10)  # Top branch

    # Draw some foliage on the branches
    pygame.draw.circle(screen, GREEN, (150, 300), 50)  # Leftmost foliage
    pygame.draw.circle(screen, DARK_GREEN, (150, 300), 30)  # Darker inner foliage

    pygame.draw.circle(screen, GREEN, (650, 300), 50)  # Rightmost foliage
    pygame.draw.circle(screen, DARK_GREEN, (650, 300), 30)  # Darker inner foliage

    pygame.draw.circle(screen, GREEN, (220, 230), 40)  # Left middle foliage
    pygame.draw.circle(screen, DARK_GREEN, (220, 230), 20)  # Darker inner foliage

    pygame.draw.circle(screen, GREEN, (580, 230), 40)  # Right middle foliage
    pygame.draw.circle(screen, DARK_GREEN, (580, 230), 20)  # Darker inner foliage

    pygame.draw.circle(screen, GREEN, (400, 170), 50)  # Top foliage
    pygame.draw.circle(screen, DARK_GREEN, (400, 170), 30)  # Darker inner foliage

    # Add dark green grass at the bottom of the tree
    pygame.draw.rect(screen, GRASS_GREEN, (0, 550, 800, 50))
    for i in range(0, 800, 40):
        pygame.draw.circle(screen, GRASS_GREEN, (i, 550), 30)


# Function to draw clouds
def draw_clouds(screen):
    # Draw clouds using circles
    pygame.draw.circle(screen, CLOUD_COLOR, (150, 100), 30)
    pygame.draw.circle(screen, CLOUD_COLOR, (180, 100), 40)
    pygame.draw.circle(screen, CLOUD_COLOR, (220, 100), 30)

    pygame.draw.circle(screen, CLOUD_COLOR, (600, 150), 30)
    pygame.draw.circle(screen, CLOUD_COLOR, (630, 150), 40)
    pygame.draw.circle(screen, CLOUD_COLOR, (670, 150), 30)

    pygame.draw.circle(screen, CLOUD_COLOR, (400, 80), 25)
    pygame.draw.circle(screen, CLOUD_COLOR, (430, 80), 35)
    pygame.draw.circle(screen, CLOUD_COLOR, (470, 80), 25)


# Create round buttons
buttons = [
    Button(200, 500, 50, "DEMO", font_default),
    Button(400, 500, 50, "4-WORDS", font_default),
    Button(600, 500, 50, "INSTRUCTIONS", font_very_small),
    Button(300, 440, 50, "5-WORDS", font_default),
    Button(500, 440, 50, "6-WORDS", font_default)
]

# Main loop
running = True
while running:
    screen.fill(SKY_BLUE)  # Sky background

    # Draw clouds
    draw_clouds(screen)

    # Draw tree
    draw_tree(screen)

    # Draw buttons (apple-like buttons)
    for button in buttons:
        button.draw(screen)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        for button in buttons:
            if button.is_clicked(event):
                print(f"{button.text} clicked!")

    # Update the display
    pygame.display.update()


pygame.quit()
sys.exit()
