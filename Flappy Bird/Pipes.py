
import pygame
from Constants import HEIGHT, PIPE_WIDTH


class Pipepair:
    
    """
    Pair of pipes that bird should passs trhough for the game
    gap_y is the top, gap height is the gap size (vertical), rest is all pipe
    
    """
    
    def __init__(self, x_pos:int, gap_y:int, gap_height:int):
        self.x_pos = x_pos
        self.gap_y = gap_y
        self.gap_height = gap_height
        self.width = PIPE_WIDTH
        
    def draw(self, screen:pygame.Surface):
        top, bottom = self.hitbox()
        pygame.draw.rect(screen, "darkgreen", top)
        pygame.draw.rect(screen, "darkgreen", bottom)
        
    def hitbox(self) -> tuple[pygame.Rect, pygame.Rect]:
            
        top_pipe = pygame.Rect(
            self.x_pos, 
            0,
            self.width, 
            self.gap_y
        )      

        bottom_pipe = pygame.Rect(
            self.x_pos, 
            self.gap_y + self.gap_height,
            self.width, 
            HEIGHT
        )
        
        return (top_pipe, bottom_pipe)