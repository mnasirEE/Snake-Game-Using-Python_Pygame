import pygame
import random
pygame.init()
pygame.mixer.init()
white = (255,255,0)
# Screen configuration
screen_width = 700
screen_height = 600
mywindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Nasir's Snake Game")

pygame.display.update()

game_ov = 0

image_s = pygame.image.load("black.jpeg")
image_s = pygame.transform.scale(image_s, (screen_width,screen_height)).convert_alpha()

# Welcome screen
image = pygame.image.load("download.jpeg")
image = pygame.transform.scale(image, (screen_width, screen_height)).convert_alpha()

def welcome_screen():
    game_exit = False
    # Music play
    pygame.mixer.music.load("osman.mp3")
    pygame.mixer.music.play(-1) 
    while not game_exit:
        mywindow.fill((233,200,245))
        # adjust image
        mywindow.blit(image,(0,0))
        screen_text("""Welcome to "Saeed" Studio""", (0,105,180), 50,10)
        screen_text("""Press Space to Play Snake Game""", (0,105,250), 25,50)
         
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("a.mp3")
                    pygame.mixer.music.play(-1)
                    # pygame.mixer.music.rewind()
                    mygame_loop()  

        pygame.display.update()
        clock.tick(fps)
        

# clock of snake game
clock = pygame.time.Clock()
# frame per second, update frame after how many seconds
fps = 30


# draw snake
def display_snake(mywindow, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(mywindow, color, [x, y, snake_size, snake_size])

# Printing score on screen

font = pygame.font.SysFont(None, 30)
def screen_text(text, color, x, y):
    
    screen_text = font.render(text, True, color)
    mywindow.blit(screen_text, [x,y])

# creating game loop
def mygame_loop():
    global game_over
    exit_game = False
    game_over = False

    # colors
    white = (255,255,255)
    yellow = (255,255,0)
    red = (255,0,0)
    green = (0,255,0)
    black = (0,0,0)

    # Snake Initial Size 
    snake_x = 35
    snake_y = 45
    snake_size = 15

    # Snake Food

    food_x = random.randint(30,screen_width - 30)
    food_y = random.randint(30,screen_height - 30)
    score = 0   

    # Velocity
    velocity_x = 0
    velocity_y = 0
    initial_velocity = 4

    # controlling snake length
    snake_list = []
    snake_length = 1

    # read Hiscore file
    with open ("hiscore.txt", "r") as h:
        hi_score = h.read()

    while not exit_game:
        if game_over:
            
            # updating high score
            with open("hiscore.txt", "w") as w:
                w.write(str(hi_score)) 

            
            mywindow.fill(black)
            
            screen_text("Game Over! Press Enter to Continue", red, 155, 170)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                       welcome_screen() 

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                # Movements of snake 
                if event.type == pygame.KEYDOWN:
                    # move right
                    if event.key == pygame.K_RIGHT:
                        velocity_x = initial_velocity
                        velocity_y = 0
                    # move left
                    if event.key == pygame.K_LEFT:
                        velocity_x = -initial_velocity
                        velocity_y = 0
                    # move up
                    if event.key == pygame.K_UP:
                        velocity_y = -initial_velocity
                        velocity_x = 0 
                    # move down
                    if event.key == pygame.K_DOWN:
                        velocity_y = initial_velocity
                        velocity_x = 0
                    # Stop Snake
                    if event.key == pygame.K_TAB:
                        velocity_x = 0
                        velocity_y = 0    
        
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            # fill screen by white color
            mywindow.fill(black) 
            mywindow.blit(image_s, (0,0))
            screen_text("    Score: " + str(score) + "          High Score: " + str(hi_score), yellow, 5,5) 
            # Draw snake
            display_snake(mywindow, green, snake_list, snake_size) 
            # Food of snake            
            pygame.draw.rect(mywindow, red, [food_x, food_y, snake_size, snake_size])  
            
        

            # increase size
            if abs(snake_x - food_x) < 8 and abs(snake_y - food_y) < 8:
                score += 5 
                food_x = random.randint(40,screen_width // 2)
                food_y = random.randint(40,screen_height // 2)
                snake_length += 4
                
            snake_head = []
            snake_head.append(snake_x)
            snake_head.append(snake_y)
            snake_list.append(snake_head)

            # Game over
            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
                # Music play
                pygame.mixer.music.load("c.mp3")
                pygame.mixer.music.play()

            # controlling length of snake
            if len(snake_list) > snake_length:
                del snake_list[0]
        # Collinding with itself
            for i in range(1,len(snake_list) - 1):
                head = snake_list[-1]
                # del snake_list[-1]
                if snake_list[i] == head:
                    game_over = True
                    # Music play
                    pygame.mixer.music.load("c.mp3")
                    pygame.mixer.music.play()
        # Updating high score
        if score > int(hi_score):
            hi_score = score
        
        # using clock
        clock.tick(fps)
        pygame.display.update()
    pygame.quit()
    quit()
   
welcome_screen() 