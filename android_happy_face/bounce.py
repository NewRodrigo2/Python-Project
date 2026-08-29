import pygame
import sys

# --- Settings ---
WIDTH, HEIGHT = 800, 600
FPS = 60
CHAR = "D"
FONT_SIZE = 48
SPEED = 5
BG_COLOR = (15, 15, 30)
CHAR_COLOR = (0, 220, 120)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Character — Press any key to quit")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Consolas", FONT_SIZE, bold=True)

# Render the character surface once
char_surf = font.render(CHAR, True, CHAR_COLOR)
cw, ch = char_surf.get_size()

# Starting position and velocity
x, y = WIDTH // 2, HEIGHT // 2
dx, dy = SPEED, SPEED

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            running = False

    # Bounce off edges
    if x <= 0:
        x = 0
        dx = abs(dx)
    elif x + cw >= WIDTH:
        x = WIDTH - cw
        dx = -abs(dx)

    if y <= 0:
        y = 0
        dy = abs(dy)
    elif y + ch >= HEIGHT:
        y = HEIGHT - ch
        dy = -abs(dy)

    x += dx
    y += dy

    # Draw
    screen.fill(BG_COLOR)
    screen.blit(char_surf, (x, y))

    # Hint text
    hint = font.render("Press any key to quit", True, (80, 80, 100))
    screen.blit(hint, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
