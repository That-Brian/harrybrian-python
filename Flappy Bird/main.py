import pygame

from Constants import WIDTH, FRAMERATE, HEIGHT


from bird import Bird

from Pipes import Pipepair

pygame.init


screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

BIRD_STARTING_X = 480
BIRD_STARTING_Y = HEIGHT // 2

bird = Bird(BIRD_STARTING_X, BIRD_STARTING_Y)
pipes = [Pipepair(700, 300, 200)]


done = False

while not done:
    #Game loop, draw, updates
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()
            
    bird.update()
            
    screen.fill("white")
    
    for pipe in pipes:
        pipe.draw(screen)
    
    bird.draw(screen)

    pygame.display.flip()
    clock.tick(FRAMERATE)
            
            
            
            
            
            
pygame.quit()