import pygame
import sys
from ai import check_winner, ai_move, is_board_full

# Initialize pygame
pygame.init()

# Set up display
WINDOW_WIDTH, WINDOW_HEIGHT = 700, 700  # Dimensions of the entire window
WIDTH, HEIGHT = 480, 480                # Dimensions of the Tic Tac Toe container
ROWS, COLS = 3, 3
SQUARE_SIZE = WIDTH // COLS
CONTAINER_X, CONTAINER_Y = 210, 90      # Position of the Tic Tac Toe container

SCALE_FACTOR = 0.5
IMAGE_SIZE = int(SQUARE_SIZE * SCALE_FACTOR)

# Load images
X_IMG = pygame.image.load('images/X.png')
O_IMG = pygame.image.load('images/O.png')
BOARD_IMG = pygame.image.load('images/Board.png')
BACKGROUND_IMG = pygame.image.load('images/Background.png')
WINNER_IMG = pygame.image.load('images/winner.png')   
LOSER_IMG = pygame.image.load('images/loser.png')     

# Scale game images
X_IMG = pygame.transform.scale(X_IMG, (IMAGE_SIZE, IMAGE_SIZE))
O_IMG = pygame.transform.scale(O_IMG, (IMAGE_SIZE, IMAGE_SIZE))
BOARD_IMG = pygame.transform.scale(BOARD_IMG, (WIDTH, HEIGHT))
BACKGROUND_IMG = pygame.transform.scale(BACKGROUND_IMG, (WINDOW_WIDTH, WINDOW_HEIGHT))

# Scale result images
RESULT_IMG_WIDTH, RESULT_IMG_HEIGHT = 300, 300  # Dimensions for result images
WINNER_IMG = pygame.transform.scale(WINNER_IMG, (RESULT_IMG_WIDTH, RESULT_IMG_HEIGHT))
LOSER_IMG = pygame.transform.scale(LOSER_IMG, (RESULT_IMG_WIDTH, RESULT_IMG_HEIGHT))

# Set up the screen
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Load sound effects and music
pygame.mixer.init()
# place_sound = pygame.mixer.Sound('sounds/place.wav')  
pygame.mixer.music.load('sounds/background.mp3')
pygame.mixer.music.play(-1)

# Board representation
board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]

# Draw board
def draw_board():
    screen.blit(BACKGROUND_IMG, (0, 0))
    screen.blit(BOARD_IMG, (CONTAINER_X, CONTAINER_Y))
    for row in range(ROWS):
        for col in range(COLS):
            x_pos = CONTAINER_X + col * SQUARE_SIZE + (SQUARE_SIZE - IMAGE_SIZE) // 2
            y_pos = CONTAINER_Y + row * SQUARE_SIZE + (SQUARE_SIZE - IMAGE_SIZE) // 2
            if board[row][col] == 'X':
                screen.blit(X_IMG, (x_pos, y_pos))
            elif board[row][col] == 'O':
                screen.blit(O_IMG, (x_pos, y_pos))
    pygame.display.update()

# Display winner or loser
def display_result(result):
    if result == 'win':
        result_img = WINNER_IMG
    else:
        result_img = LOSER_IMG

    # Calculate position to center the result image
    result_x = (WINDOW_WIDTH - RESULT_IMG_WIDTH) // 2
    result_y = (WINDOW_HEIGHT - RESULT_IMG_HEIGHT) // 2

    screen.blit(result_img, (result_x, result_y))
    pygame.display.update()

# Get row and col from mouse position
def get_row_col_from_mouse(pos):
    x, y = pos
    row = (y - CONTAINER_Y) // SQUARE_SIZE
    col = (x - CONTAINER_X) // SQUARE_SIZE
    return row, col

# Reset the game
def reset_game():
    global board, player
    board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]
    player = 'X'
    draw_board()

# Main game loop
def main():
    global board, player
    player = 'X'
    run = True
    game_over = False
    draw_board()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_over:
                    reset_game()
                    game_over = False
                else:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    if 0 <= row < ROWS and 0 <= col < COLS and board[row][col] == ' ':
                        board[row][col] = player
                        player = 'O' if player == 'X' else 'X'
                        draw_board()

        # AI's turn
        if player == 'O' and not game_over:
            ai_move_result = ai_move(board)
            if ai_move_result is not None:
                ai_row, ai_col = ai_move_result
                board[ai_row][ai_col] = 'O'
                player = 'X'
                draw_board()

        # Check for winner
        if not game_over:
            winner = check_winner(board)
            if winner:
                if winner == 'X':
                    display_result('win')
                else:
                    display_result('lose')
                game_over = True
            elif is_board_full(board):
                display_result('draw')
                game_over = True

if __name__ == "__main__":
    main()
