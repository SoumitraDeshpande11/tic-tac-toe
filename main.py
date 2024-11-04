import pygame
import sys

pygame.init()

# Screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
LINE_WIDTH = 15
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (70, 130, 180)
RED = (220, 20, 60)
BACKGROUND_COLOR = (30, 30, 30)
GRID_COLOR = (50, 50, 50)

# Fonts
FONT = pygame.font.Font(None, 100)
WIN_FONT = pygame.font.Font(None, 75)

# Initialize board
board = [['' for _ in range(3)] for _ in range(3)]
current_player = 'X'
game_over = False
winner = None

# Draw grid
def draw_grid():
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.line(screen, GRID_COLOR, (200, 0), (200, SCREEN_HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, GRID_COLOR, (400, 0), (400, SCREEN_HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, GRID_COLOR, (0, 200), (SCREEN_WIDTH, 200), LINE_WIDTH)
    pygame.draw.line(screen, GRID_COLOR, (0, 400), (SCREEN_WIDTH, 400), LINE_WIDTH)

# Draw X and O
def draw_marks():
    for row in range(3):
        for col in range(3):
            mark = board[row][col]
            if mark == 'X':
                text = FONT.render(mark, True, BLUE)
                screen.blit(text, (col * 200 + 50, row * 200 + 30))
            elif mark == 'O':
                text = FONT.render(mark, True, RED)
                screen.blit(text, (col * 200 + 50, row * 200 + 30))

# Check for win or draw
def check_winner():
    global game_over, winner
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != '':
            game_over, winner = True, board[row][0]
            return
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            game_over, winner = True, board[0][col]
            return
    if board[0][0] == board[1][1] == board[2][2] != '':
        game_over, winner = True, board[0][0]
        return
    if board[0][2] == board[1][1] == board[2][0] != '':
        game_over, winner = True, board[0][2]
        return
    if all(board[row][col] != '' for row in range(3) for col in range(3)):
        game_over, winner = True, 'Draw'

# Restart game
def restart_game():
    global board, current_player, game_over, winner
    board = [['' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    game_over = False
    winner = None

# Main game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX, mouseY = pygame.mouse.get_pos()
            clicked_row, clicked_col = mouseY // 200, mouseX // 200
            if board[clicked_row][clicked_col] == '':
                board[clicked_row][clicked_col] = current_player
                check_winner()
                current_player = 'O' if current_player == 'X' else 'X'
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart_game()

    draw_grid()
    draw_marks()
    if game_over:
        if winner != 'Draw':
            win_text = WIN_FONT.render(f"{winner} Wins!", True, WHITE)
        else:
            win_text = WIN_FONT.render("It's a Draw!", True, WHITE)
        screen.blit(win_text, (SCREEN_WIDTH // 2 - win_text.get_width() // 2, SCREEN_HEIGHT // 2 - win_text.get_height() // 2))
        restart_text = WIN_FONT.render("Press R to Restart", True, WHITE)
        screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))

    pygame.display.flip()
    clock.tick(30)
