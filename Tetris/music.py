import pygame

class Music:
    def __init__(self):
        self.current_track = None
    
    #plays if music changes
    def play(self, filepath, loop=True):
        if self.current_track != filepath:
            pygame.mixer_music.stop()
            pygame.mixer.music.load(filepath)
            if loop:
                pygame.mixer.music.play(-1)
            else:
                pygame.mixer.music.play(0)
            self.current_track = filepath

    def stop(self):
        pygame.mixer.music.stop()
        self.current_track = None

    def is_playing(self):
        return pygame.mixer.music.get_busy()