import pygame

pygame.init()

WINDOW_SIZE = (300, 300)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Tic Tac Toe")

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

player1 = 'X'
player2 = 'O'
current_player = player1

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

font = pygame.font.SysFont('Arial', 100)

def draw_board():
    pygame.draw.line(screen, BLACK, (100, 0), (100, 300), 5)
    pygame.draw.line(screen, BLACK, (200, 0), (200, 300), 5)
    pygame.draw.line(screen, BLACK, (0, 100), (300, 100), 5)
    pygame.draw.line(screen, BLACK, (0, 200), (300, 200), 5)

    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                x = col * 100
                y = row * 100
                pygame.draw.line(screen, BLUE, (x + 20, y + 20), (x + 80, y + 80), 5)
                pygame.draw.line(screen, BLUE, (x + 20, y + 80), (x + 80, y + 20), 5)
            elif board[row][col] == 'O':
                x = col * 100
                y = row * 100
                pygame.draw.circle(screen, WHITE, (x + 50, y + 50), 40, 5)

def check_win():
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != ' ':
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True

    return False

def show_winner(winner):
    text = font.render(f"{winner} wins!", True, BLACK)
    screen.blit(text, (30, 120))
    pygame.display.update()
    pygame.time.wait(2000)

def show_tie():
    text = font.render("It's a tie!", True, BLACK)
    screen.blit(text, (30, 120))

    pygame.display.update()
