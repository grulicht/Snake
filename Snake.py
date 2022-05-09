import pygame
import random
import sys

from Options import Options_Snake

def update_position(snake, direction, step):
    if direction == "UP":
        snake = [snake[0], snake[1] -step]
    if direction == "DOWN":
        snake = [snake[0], snake[1] +step]
    if direction == "LEFT":
        snake = [snake[0] - step, snake[1]]
    if direction == "RIGHT":
        snake = [snake[0] + step, snake[1]]
    return snake

def update_direction(direction, keys):
    if keys[pygame.K_LEFT]:
        return "LEFT" if direction != "RIGHT" else direction
    if keys[pygame.K_RIGHT]:
        return "RIGHT" if direction != "LEFT" else direction
    if keys[pygame.K_UP]:
        return "UP" if direction != "DOWN" else direction
    if keys[pygame.K_DOWN]:
        return "DOWN" if direction != "UP" else direction
    return direction

def is_out(snake, game_res):
    if snake[0] < 0 or snake[1] < 0 or snake[0] > game_res[0] or snake[1] > game_res[1]:
        return True
    return False

def end_game(window):
    print("GAME OVER")
    window.fill(Options_Snake.BACKGROUND_COLOR)
    pygame.quit()
    sys.exit()
   
    

def generate_apple(game_res, snake_size):
    x = random.choice(range(0, game_res[0] - snake_size + 1, snake_size))
    y = random.choice(range(0, game_res[1] - snake_size + 1, snake_size))
    return [x, y]

def is_collision(snake_head, apple):
    if snake_head[0] == apple[0] and snake_head[1] == apple[1]:
        return True
    return False


if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode(Options_Snake.GAME_RES)
    snake = [[Options_Snake.GAME_RES[0]//2, Options_Snake.GAME_RES[1]//2]]
    apple = generate_apple(Options_Snake.GAME_RES, Options_Snake.SNAKE_SIZE)
    game_font=pygame.font.SysFont("comicsans", 25)
    direction = "LEFT"
    score=""

    while True:
        score_text=game_font.render(f"Score {score}" , True, (255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys=pygame.key.get_pressed()
        direction = update_direction(direction, keys)
        new_position = update_position(snake[0], direction, Options_Snake.SNAKE_SIZE)
        snake.insert(0, new_position)
        if is_collision(snake[0], apple):
            print("Collision")
            apple = generate_apple(Options_Snake.GAME_RES, Options_Snake.SNAKE_SIZE)
            
        else:
            snake.pop()
            
        if is_out(snake[0], Options_Snake.GAME_RES):
            end_game(window)

        for part in snake:    
            pygame.draw.rect(window, Options_Snake.BODY_COLOR, pygame.Rect(part[0], part[1], Options_Snake.SNAKE_SIZE, Options_Snake.SNAKE_SIZE))
        pygame.draw.rect(window, Options_Snake.APPLE_COLOR, pygame.Rect(apple[0], apple[1], Options_Snake.SNAKE_SIZE, Options_Snake.SNAKE_SIZE))
        pygame.display.update()
        window.fill(Options_Snake.BACKGROUND_COLOR)
        window.blit(score_text, (500, 0))
        clock.tick(Options_Snake.GAME_FPS)

        