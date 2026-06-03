import pygame

from Constants import WIDTH, FRAMERATE, HEIGHT, GAME_FONT


from bird import Bird

from Pipes import Pipepair

from Pipes import create_pipe

from Pipes import PIPE_WIDTH

from game_over_screen import GameOverScreen

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()


BIRD_STARTING_X = 480
BIRD_STARTING_Y = HEIGHT // 2
GAP_BETWEEN_PIPES = 300

pipes_speed = 5
bird = Bird(BIRD_STARTING_X, BIRD_STARTING_Y)
pipes:list[Pipepair] = []
score = 0
score_text = pygame.Surface((0,0))

def set_score(new_score:int):
    global score, score_text
    score = new_score
    score_text = GAME_FONT.render(f"score:{score}", True, "black")
    
set_score(0)

def manage_pipes():
    """generate, moving and deleting pipes"""
    
    for pipe in pipes:
        pipe.move(pipes_speed)
    
    can_generate_new_pipe = len(pipes) == 0 or WIDTH - pipes[-1].x_pos >= GAP_BETWEEN_PIPES + PIPE_WIDTH
    if can_generate_new_pipe: 
        new_pipe = create_pipe()
        pipes.append(new_pipe)
        
    pipes_x = pipes[0].x_pos
    if pipes_x < -PIPE_WIDTH:
        pipes.pop(0)
    
def reset_game():
    global bird, pipes, score, score_text
    pipes = []
    bird = Bird(BIRD_STARTING_X, BIRD_STARTING_Y)
    set_score(0)
      

done = False

while not done:
    # game loop
    
    # process player events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()
            if event.key == pygame.K_ESCAPE:
                reset_game()
    
    # update logic and physics
    if not bird.dead:
        bird.update(pipes)
        manage_pipes()
        
        if bird.has_passed_pipe(pipes):
            score += 1
            set_score(score + 1)
    
    # draw stuff!
    screen.fill("white")  # todo: hex codes

    if bird.dead:
        screen.fill(0xff7777)
    
    for pipe in pipes:
        pipe.draw(screen)
    
    bird.draw(screen)
    
    score_text_hitbox = score_text.get_rect(center=(WIDTH //2, 48))
    screen.blit(score_text, score_text_hitbox)
    
    pygame.display.flip()
    clock.tick(FRAMERATE)    
            
            
            
            
            
            
pygame.quit()