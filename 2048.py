import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
width, height = 400, 400
gridSize = 4
gridCellSize = width // gridSize
gridColor = (187, 173, 160)
fontSize = 36
backgroundColor = (205, 193, 180)

# Fonts
font = pygame.font.Font(None, fontSize)

# Initialize the grid
grid = [[0 for _ in range(gridSize)] for _ in range(gridSize)]

# Number colors and box colors
numberColors = {
    0: (205, 193, 180),  # Empty cell
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46)
}

boxColor = (172, 156, 141)


# Function to draw the grid
def draw_grid(screen):
    screen.fill(backgroundColor)
    for row in range(gridSize):
        for col in range(gridSize):
            pygame.draw.rect(screen, gridColor, (col * gridCellSize, row * gridCellSize, gridCellSize, gridCellSize), 0)
            number = grid[row][col]
            if number > 0:
                pygame.draw.rect(screen, numberColors[number], (col * gridCellSize, row * gridCellSize, gridCellSize, gridCellSize), 0)
                text = font.render(str(number), True, (0, 0, 0))
                text_rect = text.get_rect(center=(col * gridCellSize + gridCellSize // 2, row * gridCellSize + gridCellSize // 2))
                pygame.draw.rect(screen, boxColor, (col * gridCellSize, row * gridCellSize, gridCellSize, gridCellSize), 3)
                screen.blit(text, text_rect)


# Function to add a random tile (2 or 4) to the grid
def add_random_tile():
    emptyCells = [(row, col) for row in range(gridSize) for col in range(gridSize) if grid[row][col] == 0]
    if emptyCells:
        row, col = random.choice(emptyCells)
        grid[row][col] = random.choice([2, 4])


# Function to check for a win (2048 in any cell)
def check_win():
    for row in range(gridSize):
        for col in range(gridSize):
            if grid[row][col] == 2048:
                return True
    return False


# Function to check for a loss (no empty cells) (hard mode)
def check_loss_hard():
    for row in range(gridSize):
        for col in range(gridSize):
            if grid[row][col] == 0:
                return False  # There is an empty cell, game can continue
    return True  # No empty cells, you lost


# Function to check for a loss (no empty cells and no available moves) (easy mode)
def check_loss_easy():
    for row in range(gridSize):
        for col in range(gridSize):
            if grid[row][col] == 0:
                return False  # There is an empty cell, game can continue

            if col < gridSize - 1 and (grid[row][col] == grid[row][col + 1] or grid[row][col] == 0):
                return False  # Tiles can merge horizontally or there is an empty cell

            if row < gridSize - 1 and (grid[row][col] == grid[row + 1][col] or grid[row][col] == 0):
                return False  # Tiles can merge vertically or there is an empty cell

    return True  # No empty cells and no available moves


# Function to display the menu and select game mode
def show_menu():
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("2048 Game - Select Mode")
    
    menu_running = True
    selected_mode = None
    
    while menu_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 100 <= event.pos[0] <= 300 and 200 <= event.pos[1] <= 250:
                    selected_mode = "easy"
                    menu_running = False
                elif 100 <= event.pos[0] <= 300 and 300 <= event.pos[1] <= 350:
                    selected_mode = "hard"
                    menu_running = False
        
        # Draw the menu
        screen.fill(backgroundColor)
        title_font = pygame.font.Font(None, 48)
        title_text = title_font.render("2048 Game", True, (0, 0, 0))
        title_rect = title_text.get_rect(center=(width // 2, height // 4))

        easy_button = pygame.Rect(100, 200, 200, 50)
        easy_font = pygame.font.Font(None, 36)
        easy_text = easy_font.render("Easy Mode", True, (0, 0, 0))
        easy_text_rect = easy_text.get_rect(center=easy_button.center)

        hard_button = pygame.Rect(100, 300, 200, 50)
        hard_font = pygame.font.Font(None, 36)
        hard_text = hard_font.render("Hard Mode", True, (0, 0, 0))
        hard_text_rect = hard_text.get_rect(center=hard_button.center)

        pygame.draw.rect(screen, (0, 0, 0), easy_button, 2)
        pygame.draw.rect(screen, (0, 0, 0), hard_button, 2)

        screen.blit(title_text, title_rect)
        screen.blit(easy_text, easy_text_rect)
        screen.blit(hard_text, hard_text_rect)

        pygame.display.flip()

    return selected_mode

# Display the menu and select game mode
game_mode = show_menu()

# Create a window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("2048 Game")

# Initialize the game
add_random_tile()
add_random_tile()


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # Implement left movement logic
                for row in range(gridSize):
                    # Merge tiles
                    for col in range(1, gridSize):
                        if grid[row][col] != 0:
                            for move_col in range(col, 0, -1):
                                if grid[row][move_col - 1] == 0:
                                    grid[row][move_col - 1] = grid[row][move_col]
                                    grid[row][move_col] = 0
                                elif grid[row][move_col - 1] == grid[row][move_col]:
                                    grid[row][move_col - 1] *= 2
                                    grid[row][move_col] = 0
                                    # Update score here if needed
                                    break

            elif event.key == pygame.K_RIGHT:
                # Implement right movement logic
                for row in range(gridSize):
                    # Merge tiles
                    for col in range(gridSize - 2, -1, -1):
                        if grid[row][col] != 0:
                            for move_col in range(col, gridSize - 1):
                                if grid[row][move_col + 1] == 0:
                                    grid[row][move_col + 1] = grid[row][move_col]
                                    grid[row][move_col] = 0
                                elif grid[row][move_col + 1] == grid[row][move_col]:
                                    grid[row][move_col + 1] *= 2
                                    grid[row][move_col] = 0
                                    # Update score here if needed
                                    break

            elif event.key == pygame.K_UP:
                # Implement up movement logic
                for col in range(gridSize):
                    # Merge tiles (if able to)
                    for row in range(1, gridSize):
                        if grid[row][col] != 0:
                            for move_row in range(row, 0, -1):
                                if grid[move_row - 1][col] == 0:
                                    grid[move_row - 1][col] = grid[move_row][col]
                                    grid[move_row][col] = 0
                                elif grid[move_row - 1][col] == grid[move_row][col]:
                                    grid[move_row - 1][col] *= 2
                                    grid[move_row][col] = 0
                                    # Update score here if needed
                                    break

            elif event.key == pygame.K_DOWN:
                # Implement down movement logic
                for col in range(gridSize):
                    # Merge tiles (if able to)
                    for row in range(gridSize - 2, -1, -1):
                        if grid[row][col] != 0:
                            for move_row in range(row, gridSize - 1):
                                if grid[move_row + 1][col] == 0:
                                    grid[move_row + 1][col] = grid[move_row][col]
                                    grid[move_row][col] = 0
                                elif grid[move_row + 1][col] == grid[move_row][col]:
                                    grid[move_row + 1][col] *= 2
                                    grid[move_row][col] = 0
                                    # Update score here if needed
                                    break

            # After each move, add a random tile and update the display
            add_random_tile()
            draw_grid(screen)
            pygame.display.flip()

            # Check for win or loss based on the selected game mode
            if game_mode == "easy" and check_loss_easy():
                print("You lose!")
                running = False
            elif game_mode == "hard" and check_loss_hard():
                print("You lose!")
                running = False
            elif check_win():
                print("You win!")
                running = False

# Quit Pygame
pygame.quit()

