import pygame
import random
import time


pygame.init()


WIDTH, HEIGHT = 400, 400
CARD_SIZE = 80
GRID_SIZE = 4
MARGIN = 10
FPS = 30
TIME_LIMIT = 60 


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Memory Puzzle Game")
clock = pygame.time.Clock()


colors = [RED, BLUE, GREEN, YELLOW, ORANGE, (0, 255, 255), (255, 105, 180), (128, 0, 128)]
colors *= 2  
random.shuffle(colors)  


cards = []
for i in range(GRID_SIZE):
    row = []
    for j in range(GRID_SIZE):
        row.append({
            "color": colors.pop(),
            "visible": False,
            "matched": False
        })
    cards.append(row)

def draw_grid():
    """Draws the grid of cards."""
    screen.fill(WHITE)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            card = cards[i][j]
            x = j * (CARD_SIZE + MARGIN)
            y = i * (CARD_SIZE + MARGIN)
            if card["visible"] or card["matched"]:
                pygame.draw.rect(screen, card["color"], (x, y, CARD_SIZE, CARD_SIZE))
            else:
                pygame.draw.rect(screen, BLACK, (x, y, CARD_SIZE, CARD_SIZE))

def get_card_at_pos(pos):
    """Returns the card based on mouse position."""
    x, y = pos
    row = y // (CARD_SIZE + MARGIN)
    col = x // (CARD_SIZE + MARGIN)
    if row < GRID_SIZE and col < GRID_SIZE:
        return cards[row][col]
    return None


first_card = None
second_card = None
game_over = False
start_time = time.time()


while not game_over:
    elapsed_time = int(time.time() - start_time)
    if elapsed_time > TIME_LIMIT:
        print("Time's up! You lost.")
        game_over = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            card = get_card_at_pos(pygame.mouse.get_pos())
            if card and not card["visible"] and not card["matched"]:
                card["visible"] = True
                if not first_card:
                    first_card = card
                elif not second_card:
                    second_card = card

                    
                    if first_card["color"] == second_card["color"]:
                        print("Matched!")
                        first_card["matched"] = True
                        second_card["matched"] = True
                    else:
                        pygame.display.flip()
                        time.sleep(1)  
                        first_card["visible"] = False
                        second_card["visible"] = False

                    first_card = None
                    second_card = None

    
    draw_grid()


    font = pygame.font.Font(None, 36)
    timer_text = font.render(f"Time left: {TIME_LIMIT - elapsed_time}s", True, BLACK)
    screen.blit(timer_text, (10, 10))

    
    if all(card["matched"] for row in cards for card in row):
        print("You won!")
        game_over = True

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
