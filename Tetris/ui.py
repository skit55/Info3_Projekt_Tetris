import pygame
from colors import Colors

class UI:
    def __init__(self, game, screen):
        self.game = game
        self.screen = screen
        self.title_font = pygame.font.Font(None, 40)
        self.text_font = pygame.font.Font(None, 20)

        self.score_rect = pygame.Rect(320, 55, 170, 60)
        self.highscore_rect = pygame.Rect(320, 220, 170, 50)
        self.next_rect = pygame.Rect(320, 335, 170, 180)

    def draw(self):
        
        score_label = self.title_font.render("Score", True, Colors.black)
        next_label = self.title_font.render("Next", True, Colors.black)
        highscore_label = self.title_font.render("Highscore", True, Colors.black)
        self.screen.blit(score_label, (365, 20, 50, 50))
        self.screen.blit(highscore_label, (335, 190, 50, 50))
        self.screen.blit(next_label, (375, 300, 50, 50))

        
        pygame.draw.rect(self.screen, Colors.brown, self.score_rect, 0, 10)
        score_value = self.title_font.render(str(self.game.score), True, Colors.black)
        self.screen.blit(score_value, score_value.get_rect(center=self.score_rect.center))

        
        pygame.draw.rect(self.screen, Colors.brown, self.highscore_rect, 0, 10)
        hs_value = self.title_font.render(str(self.game.highscore), True, Colors.black)
        self.screen.blit(hs_value, hs_value.get_rect(center=self.highscore_rect.center))

        
        pygame.draw.rect(self.screen, Colors.brown, self.next_rect, 0, 10)
        if self.game.next_block.id == 3:
            self.game.next_block.draw(self.screen, 255, 290)
        elif self.game.next_block.id == 4:
            self.game.next_block.draw(self.screen, 255, 280)
        else:
            self.game.next_block.draw(self.screen, 270, 270)
