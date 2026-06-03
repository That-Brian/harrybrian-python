import pygame
from Constants import HEIGHT
from Pipes import Pipepair

HITBOX_RADIUS = 30
GRAVITY = 0.5 # in pixels per frames^2
TERMINAL_VELOCITY = 10
JUMP_STRENGTH = -8


class Bird:
    
    def __init__(self, initial_x:int, initial_y: int) -> None:
        self.centre_x = initial_x
        self.centre_y = initial_y # y goes further down screen as y value increases
        self.radius = 30
        self.velocity_y = 0
        self.dead = False
    
    def draw(self, screen:pygame.Surface):
        pygame.draw.rect(screen, "red", self.hitbox())
        
    def update(self, pipes:list[Pipepair]):
        hitbox = self.hitbox()
        
        self.centre_y += self.velocity_y
        self.velocity_y += GRAVITY
        self.velocity_y = min(self.velocity_y, TERMINAL_VELOCITY) 
        # prevent bird from exceeding terminal velocity
        
        if hitbox.bottom >= HEIGHT and self.velocity_y > 0:
            self.dead = True
        
        if hitbox.top <= 0 and self.velocity_y < 0:
            self.dead = True
            
            
    def jump(self):
        self.velocity_y = JUMP_STRENGTH
        
        
    def hitbox(self) -> pygame.Rect:
        return pygame.Rect(
            self.centre_x - self.radius, #left
            self.centre_y - self.radius, # right 
            2*self.radius,
            2*self.radius,
        )
    
    def has_hit_pipe(self, pipe_list:list[Pipepair]) -> bool:
        
        bird_hitbox = self.hitbox()
        
        for pipe in pipe_list:
            pipe_hitbox = pipe.hitbox()
            hit = bird_hitbox.colliderect(pipe_hitbox[0]) or bird_hitbox.colliderect(pipe_hitbox[1])
            if hit:
                return True
            
        return False
    
    def has_passed_pipe(self, pipe_list:list[Pipepair]) -> bool:
        hitbox = self.hitbox()
        for pipe in pipe_list:
            if not pipe.passed and hitbox.x > pipe.x_pos + pipe.width:
                pipe.passed = True
                return True
        return False