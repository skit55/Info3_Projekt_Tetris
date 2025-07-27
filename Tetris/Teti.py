import sys
import pygame
from game import Game
from colors import Colors
from button import Button
from music import Music

pygame.init()

BG = pygame.image.load("Tetris/Img/Cat_background.png")
BG_hard = pygame.image.load("Tetris/Img/Nyan.jpg")


title_font = pygame.font.Font(None, 40)
text_font = pygame.font.Font(None, 20)
option_font = pygame.font.Font(None, 30)

score_surface = title_font.render("Score", True, Colors.black)
highscore_surface = title_font.render("Highscore", True, Colors.black)
next_surface = title_font.render("Next", True, Colors.black)
game_over_surface = title_font.render("GAME OVER", True, Colors.black)
restart_surface = text_font.render("Press move Button to restart", True, Colors.purple)

score_rect = pygame.Rect(320, 55, 170, 60)
highscore_rect = pygame.Rect(320, 220, 170, 50)
next_rect = pygame.Rect(320, 335, 170, 180)#-215
screen = pygame.display.set_mode((500,620))

clock = pygame.time.Clock()

music = Music()

game = Game()

game_update = pygame.USEREVENT
pygame.time.set_timer(game_update, 200)

def mainmenu():
    pygame.display.set_caption("Menu")
    screen.blit(BG, (0,0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.check_for_input(menu_mouse_pos):
                    play(275)
                if hard_button.check_for_input(menu_mouse_pos):
                    play(175)
                if quit_button.check_for_input(menu_mouse_pos):
                    pygame.quit
                    sys.exit()

        menu_mouse_pos = pygame.mouse.get_pos()
        
        Menu_Text = title_font.render("CHOOSE YOUR LVL", True, Colors.black)
        menu_rect = Menu_Text.get_rect(center=(250,100))

        #buttons
        easy_button = Button(image=None, pos=(250,250), text_input="ESAY", font=option_font, base_color=Colors.black, hovering_color=Colors.dark_green)
        hard_button = Button(image=None, pos=(250,350), text_input="HARD", font=option_font, base_color=Colors.black, hovering_color=Colors.dark_green)
        quit_button = Button(image=None, pos=(250,450), text_input="QUIT", font=option_font, base_color=Colors.black, hovering_color=Colors.dark_green)
        
        screen.blit(Menu_Text,menu_rect)

        for button in [easy_button, hard_button, quit_button]:
            button.change_color(menu_mouse_pos)
            button.update(screen)

        pygame.display.update()


def play(speed):
    pygame.display.set_caption("Tetris")
    pygame.time.set_timer(game_update, speed)
    
    #gamemode
    if speed > 180:
            track_path = "Tetris/Sound/Karma(Electric Fountain).mp3"
            screen.blit(BG, (0,0))
    else:
            track_path = "Tetris/Sound/nyan.mp3"
            screen.blit(BG_hard, (0,0))
    music.play(track_path)
    
    #gameloop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if game.game_over == True:
                    game.game_over = False
                    game.restart()
                    music.play(track_path)
                if event.key == pygame.K_LEFT and game.game_over == False:
                    game.move_left()
                if event.key == pygame.K_RIGHT and game.game_over == False:
                    game.move_right()
                if event.key == pygame.K_DOWN and game.game_over == False:
                    game.move_down()
                    game.update_score(0,1)
                if event.key == pygame.K_UP and game.game_over == False:
                    game.rotate()
            if event.type == game_update and game.game_over == False:
                game.move_down()

        if game.game_over == True:
            screen.blit(game_over_surface, (320, 550, 50 ,50))
            screen.blit(restart_surface,(315, 600, 50, 50))
            
            if game.game_over_played == False:
                music.stop()
                music.play("Tetris/Sound/gameover.mp3", False)
                game.game_over_played = True
        else:
            if speed > 180:
                screen.blit(BG, (0, 0))
            else:
                screen.blit(BG_hard, (0, 0))

        screen.blit(score_surface, (365, 20, 50, 50))
        screen.blit(highscore_surface, (335, 190, 50, 50))
        screen.blit(next_surface, (375, 300, 50, 50))

        #score
        pygame.draw.rect(screen, Colors.brown, score_rect, 0 , 10)
        score_value_surface = title_font.render(str(game.score), True, Colors.black)
        screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx,centery = score_rect.centery))
        
        #highscore
        pygame.draw.rect(screen,Colors.brown, highscore_rect,0 ,10)
        highscore_value_surface = title_font.render(str(game.highscore), True, Colors.black)
        screen.blit(highscore_value_surface, highscore_value_surface.get_rect(centerx = highscore_rect.centerx,centery = highscore_rect.centery))
        
        #next
        pygame.draw.rect(screen, Colors.brown, next_rect, 0, 10)
        game.draw(screen)

        pygame.display.update()
        clock.tick(60)

mainmenu()