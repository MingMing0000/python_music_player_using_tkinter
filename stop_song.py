# import the files needed
import pygame
from music_controls import MusicControls
from tkinter import *

# create a class StopSong that inherits from the class MusicControls
class StopSong(MusicControls):
    def __init__(self, player):
        self.player = player
        self.status = player.status
    
    def _MusicControls__set_status(self):
        self.status.set("-Stopped")
    
    def stop_song(self):
        pygame.mixer.music.stop()