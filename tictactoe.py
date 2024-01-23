import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BOARD_SIZE = 3
SQUARE_SIZE = WIDTH // BOARD_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Fonts
font = pygame.font.SysFont(None, 55)

# Function to draw the grid
def draw_grid():
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(screen, WHITE, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, WHITE, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)

# Function to draw X or O
def draw_x_o(row, col, player):
    x = col * SQUARE_SIZE + SQUARE_SIZE // 2
    y = row * SQUARE_SIZE + SQUARE_SIZE // 2

    if player == 1:
        pygame.draw.line(screen, WHITE, (x - 50, y - 50), (x + 50, y + 50), LINE_WIDTH)
        pygame.draw.line(screen, WHITE, (x + 50, y - 50), (x - 50, y + 50), LINE_WIDTH)
    else:
        pygame.draw.circle(screen, WHITE, (x, y), 50, LINE_WIDTH)

# Function to check if a player has won
def check_winner(board, player):
    # Check rows and columns
    for i in range(BOARD_SIZE):
        if all(board[i][j] == player for j in range(BOARD_SIZE)) or all(board[j][i] == player for j in range(BOARD_SIZE)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(BOARD_SIZE)) or all(board[i][BOARD_SIZE - 1 - i] == player for i in range(BOARD_SIZE)):
        return True

    return False

# Function to check if the board is full
def is_board_full(board):
    return all(board[i][j] != 0 for i in range(BOARD_SIZE) for j in range(BOARD_SIZE))

# Main game loop
def main():
    board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    player_turn = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_turn == 1:
                    col = event.pos[0] // SQUARE_SIZE
                    row = event.pos[1] // SQUARE_SIZE

                    if board[row][col] == 0:
                        board[row][col] = player_turn
                        player_turn = 2

        screen.fill(BLACK)
        draw_grid()

        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if board[row][col] == 1:
                    draw_x_o(row, col, 1)
                elif board[row][col] == 2:
                    draw_x_o(row, col, 2)

        if check_winner(board, 1):
            text = font.render("Player 1 wins!", True, WHITE)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        elif check_winner(board, 2):
            text = font.render("Player 2 wins!", True, WHITE)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        elif is_board_full(board):
            text = font.render("It's a draw!", True, WHITE)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

        pygame.display.flip()

# Run the game
if __name__ == "__main__":
    main()
