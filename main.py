import pygame
import random

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up display
WIDTH = 800
HEIGHT = 600
BORDER = 10
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Breakout Game')

# Paddle
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
PADDLE_COLOR = GREEN
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - PADDLE_HEIGHT - BORDER, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball
BALL_SIZE = 15
BALL_COLOR = RED
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_speed_x = random.choice([-5, -3, 3, 5])
ball_speed_y = random.choice([-5, -3, 3, 5])

# Bricks
BRICK_ROWS = 5
BRICK_COLUMNS = 7
BRICK_WIDTH = 80
BRICK_HEIGHT = 20
BRICK_GAP = 2
BRICK_COLORS = [(255, 0, 0), (255, 128, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (128, 0, 255)]
bricks = []
for i in range(BRICK_ROWS):
    y = BORDER + i * (BRICK_HEIGHT + BRICK_GAP)
    for j in range(BRICK_COLUMNS):
        x = BORDER + j * (BRICK_WIDTH + BRICK_GAP)
        color = BRICK_COLORS[i % len(BRICK_COLORS)]
        bricks.append(pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle.x -= 20
            if event.key == pygame.K_RIGHT:
                paddle.x += 20

    # Keep paddle within screen
    paddle.x = max(paddle.x, BORDER)
    paddle.x = min(paddle.x, WIDTH - PADDLE_WIDTH - BORDER)

    # Move ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Check for collisions
    if ball.y <= BORDER or ball.y + BALL_SIZE >= HEIGHT - PADDLE_HEIGHT - BORDER:
        ball_speed_y = -ball_speed_y
    if ball.x <= BORDER or ball.x + BALL_SIZE >= WIDTH - PADDLE_WIDTH - BORDER:
        ball_speed_x = -ball_speed_x
    if ball.y + BALL_SIZE >= paddle.y and ball.x + BALL_SIZE // 2 >= paddle.x and ball.x + BALL_SIZE // 2 <= paddle.x + PADDLE_WIDTH:
        ball_speed_y = -ball_speed_y
    for brick in bricks:
        if ball.colliderect(brick):
            ball_speed_y = -ball_speed_y
            bricks.remove(brick)
            break

    # Drawing
    DISPLAY.fill(WHITE)
    pygame.draw.rect(DISPLAY, PADDLE_COLOR, paddle)
    pygame.draw.ellipse(DISPLAY, BALL_COLOR, ball)
    for brick in bricks:
        pygame.draw.rect(DISPLAY, brick.color, brick)
    pygame.display.flip()

    # Pause briefly to control game speed
    pygame.time.delay(20)