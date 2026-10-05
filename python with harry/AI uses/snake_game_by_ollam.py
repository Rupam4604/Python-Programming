# We are going to create a classic Snake game using Pygame.
#  The game will have:
#    - A snake that the player controls.
#    - Food that the snake can eat to grow longer.
#    - The snake grows when it eats food.
#    - The game ends if the snake hits the window boundaries or itself.

#  Steps:
#    1. Initialize Pygame and set up the display window.
#    2. Define the game variables (snake position, direction, food, score, etc.).
#    3. Create a game loop that handles events, updates the game state, and draws the screen.

#  We'll use:
#    - Grid-based movement for the snake (each segment moves one grid at a time).
#    - The snake will be represented as a list of (x, y) positions on the grid.
#    - The food will be placed at random grid positions.

#  Let's set the grid size to 20x20 (each cell is 20 pixels) and the window to 400x400.

#  We'll use the arrow keys to change the direction.

#  The game will run at 10 frames per second (fps) but the snake will move every 0.15 seconds (so 6 movement per second).

#  We'll keep track of the score (each food eaten increases the score by 1) and display it.

#  We'll also include a game over screen that shows the score and waits for a key press to restart.

#  Let's break down the code:

#    - Import necessary modules.
#    - Initialize Pygame.
#    - Set up the main window.
#    - Define colors and constants (like grid size, block size, etc.).
#    - Set up the clock to control the game speed.

#    - Define functions:
#         - `draw_grid()`: Draws the grid lines (optional, for better visualization).
#         - `main()`: The main game loop.

#    - In the main loop:
#         - Handle events (key presses, quit event).
#         - Change the snake's direction based on the arrow keys, but not allow reversing.
#         - Move the snake by adding a new head in the direction of movement and removing the tail (unless it eats food).
#         - Check for collisions with food, boundaries, or itself.
#         - Update the score and food position.

#    - After game over, display the score and wait for a space bar to restart.

#  Let's code accordingly.
# ...done thinking.


# Snake Game in Python

# Here's a complete Snake game implementation using Pygame. This game includes all the classic Snake mechanics: growing
# when you eat food, game over when you hit walls or yourself, and score tracking.

# ```python
import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
FPS = 10

# Colors
BACKGROUND = (15, 15, 30)
GRID_COLOR = (40, 40, 60)
SNAKE_COLOR = (50, 205, 50)
SNAKE_HEAD_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 50, 50)
TEXT_COLOR = (200, 200, 220)
GAME_OVER_BG = (0, 0, 0, 180)  # Semi-transparent black

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake:
    def __init__(self):
        self.reset()

    def reset(self):
        self.length = 1
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.score = 0
        self.grow_to = 3  # Start with a snake of length 3

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        # Don't allow turning directly opposite to current direction
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        self.direction = point

    def move(self):
        head = self.get_head_position()
        x, y = self.direction
        new_x = (head[0] + x) % GRID_WIDTH
        new_y = (head[1] + y) % GRID_HEIGHT
        new_position = (new_x, new_y)

        # Check if snake collides with itself
        if new_position in self.positions[1:]:
            self.reset()
            return True  # Game over

        self.positions.insert(0, new_position)

        # Check if snake should grow
        if self.length < self.grow_to:
            self.length += 1
        else:
            self.positions.pop()

        return False  # Game continues

    def draw(self, surface):
        for i, p in enumerate(self.positions):
            rect = pygame.Rect((p[0] * GRID_SIZE, p[1] * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
            if i == 0:  # Head is a different color
                pygame.draw.rect(surface, SNAKE_HEAD_COLOR, rect)
                pygame.draw.rect(surface, (0, 0, 0), rect, 1)
            else:
                pygame.draw.rect(surface, SNAKE_COLOR, rect)
                pygame.draw.rect(surface, (0, 0, 0), rect, 1)

    def grow(self):
        self.grow_to += 1

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1),
                         random.randint(0, GRID_HEIGHT - 1))

    def draw(self, surface):
        rect = pygame.Rect((self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE),
                           (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, FOOD_COLOR, rect)
        pygame.draw.rect(surface, (0, 0, 0), rect, 1)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('arial', 25)
        self.snake = Snake()
        self.food = Food()
        self.game_over = False

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.snake.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.snake.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.snake.turn(RIGHT)
                elif event.key == pygame.K_r and self.game_over:
                    self.reset_game()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    def reset_game(self):
        self.snake.reset()
        self.food.randomize_position()
        self.game_over = False

    def draw_grid(self):
        for x in range(0, WIDTH, GRID_SIZE):
            pygame.draw.line(self.screen, GRID_COLOR, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, GRID_SIZE):
            pygame.draw.line(self.screen, GRID_COLOR, (0, y), (WIDTH, y))

    def draw_score(self):
        score_text = self.font.render(f'Score: {self.snake.score}', True, TEXT_COLOR)
        self.screen.blit(score_text, (10, 10))

        # Draw instructions
        instructions = self.font.render('Press ESC to quit, R to restart', True, TEXT_COLOR)
        self.screen.blit(instructions, (WIDTH - instructions.get_width() - 10, 10))

    def draw_game_over(self):
        # Create a semi-transparent overlay
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill(GAME_OVER_BG)
        self.screen.blit(overlay, (0, 0))

        # Game over text
        game_over_text = self.font.render('GAME OVER!', True, (255, 50, 50))
        self.screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2,
                                          HEIGHT // 2 - game_over_text.get_height() - 20))

        # Final score
        final_score = self.font.render(f'Final Score: {self.snake.score}', True, TEXT_COLOR)
        self.screen.blit(final_score, (WIDTH // 2 - final_score.get_width() // 2,
                                      HEIGHT // 2 + 10))

        # Restart instruction
        restart_text = self.font.render('Press R to restart', True, TEXT_COLOR)
        self.screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2,
                                       HEIGHT // 2 + 60))

    def update(self):
        if not self.game_over:
            self.game_over = self.snake.move()

            # Check if snake ate the food
            if self.snake.get_head_position() == self.food.position:
                self.snake.grow()
                self.snake.score += 10
                self.food.randomize_position()
                # Make sure food doesn't appear on snake
                while self.food.position in self.snake.positions:
                    self.food.randomize_position()

    def draw(self):
        self.screen.fill(BACKGROUND)
        self.draw_grid()
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        self.draw_score()

        if self.game_over:
            self.draw_game_over()

        pygame.display.update()

    def run(self):
        while True:
            self.handle_keys()
            self.update()
            self.draw()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.run()


# ## How to Play

# 1. Use the arrow keys (UP, DOWN, LEFT, RIGHT) to control the snake's direction.
# 2. The snake grows longer each time it eats food.
# 3. Avoid hitting the walls or the snake's own body.
# 4. When the game ends, press 'R' to restart.
# 5. Press 'ESC' to quit the game.

# ## Game Features

# - The snake wraps around the screen edges
# - Score increases by 10 points for each food eaten
# - Game shows a semi-transparent overlay during game over
# - Clear instructions displayed on the screen
# - The snake starts with a length of 3 segments

# ## Requirements

# To run this game, you need to have Python and Pygame installed. If you don't have Pygame, you can install it with:

# ```
# pip install pygame
# ```

# This implementation provides a complete, playable Snake game with clean visuals and intuitive controls. The game runs at
# a speed of 10 frames per second, which is appropriate for the classic Snake gameplay.