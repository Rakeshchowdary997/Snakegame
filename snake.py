import pygame
import time
import random


pygame.init()


width = 600
height = 400


white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

block_size = 10


font = pygame.font.SysFont("bahnschrift", 25)

clock = pygame.time.Clock()


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

def draw_snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, green, [block[0], block[1], block_size, block_size])

def game_loop():
    game_over = False
    game_close = False
    
   
    x = width / 2
    y = height / 2
    
    x_change = 0
    y_change = 0
    
    snake_list = []
    snake_length = 1
    
    food_x = random.randrange(0, width - block_size, block_size)
    food_y = random.randrange(0, height - block_size, block_size)
    
    while not game_over:
        while game_close:

            message = font.render("Game Over! Press C to Play Again or Q to Quit", True, red)
            screen.blit(message, [width / 10, height / 3])
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = block_size
                    x_change = 0
        
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True
        
        x += x_change
        y += y_change
        screen.fill(black)   

        pygame.draw.rect(screen, red, [food_x, food_y, block_size, block_size])
        
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        
        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True
        
        draw_snake(block_size, snake_list)
        pygame.display.update()
  
        if x == food_x and y == food_y:
            food_x = random.randrange(0, width - block_size, block_size)
            food_y = random.randrange(0, height - block_size, block_size)
            snake_length += 1
        
        clock.tick(10)  
    
    pygame.quit()
    quit()

game_loop()
