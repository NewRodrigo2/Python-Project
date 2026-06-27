import pygame
import sys
import math

# --- Settings ---
WIDTH, HEIGHT = 400, 400
FPS = 60
BG_COLOR = (255, 223, 100)   # sunny yellow background

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Happy Face")
clock = pygame.time.Clock()

# Animation: gentle bobbing
tick = 0

def draw_happy_face(surface, cx, cy, radius, offset_y=0):
    cy += offset_y

    # --- Face circle ---
    pygame.draw.circle(surface, (255, 220, 50), (cx, cy), radius)          # fill
    pygame.draw.circle(surface, (200, 150, 0), (cx, cy), radius, 4)        # outline

    # --- Eyes ---
    eye_offset_x = radius // 3
    eye_offset_y = radius // 5
    eye_radius = radius // 8

    for ex in [cx - eye_offset_x, cx + eye_offset_x]:
        pygame.draw.circle(surface, (50, 30, 10), (ex, cy - eye_offset_y), eye_radius)

    # --- Smile (arc drawn as a series of points) ---
    smile_rect = pygame.Rect(
        cx - radius // 2,
        cy,
        radius,
        radius // 2
    )
    pygame.draw.arc(surface, (180, 80, 0), smile_rect, math.pi, 2 * math.pi, 4)

    # --- Rosy cheeks ---
    cheek_color = (255, 160, 130, 120)
    cheek_surf = pygame.Surface((radius // 2, radius // 4), pygame.SRCALPHA)
    cheek_surf.fill((0, 0, 0, 0))
    pygame.draw.ellipse(cheek_surf, cheek_color, cheek_surf.get_rect())
    cheek_y = cy + radius // 10
    surface.blit(cheek_surf, (cx - radius // 2 - radius // 8, cheek_y))
    surface.blit(cheek_surf, (cx + radius // 8, cheek_y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            running = False

    tick += 1

    # Gentle bob: ±6 pixels using a sine wave
    bob = int(6 * math.sin(tick * 0.05))

    screen.fill(BG_COLOR)
    draw_happy_face(screen, WIDTH // 2, HEIGHT // 2, 130, offset_y=bob)

    # Hint text
    font = pygame.font.SysFont("Arial", 18)
    hint = font.render("Press any key to quit", True, (180, 130, 0))
    screen.blit(hint, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
