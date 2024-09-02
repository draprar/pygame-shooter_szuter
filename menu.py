import sys
import pygame
import tkinter as tk
from tkinter import filedialog


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.ascii_logo = """
        
     _____        _____        _____         _____        _____        _____     
  __|___  |__  __|___  |__  __|  _  |__  ___|__   |__  __|___  |__  __|__   |__  
 |   ___|    ||___   |    ||  | | |    ||_    _|     ||   ___|    ||     |     | 
  `-.`-.     | .-`.-`     ||  |_| |    | |    |      ||   ___|    ||     \     | 
 |______|  __||______|  __||______|  __| |____|    __||______|  __||__|\__\  __| 
    |_____|      |_____|      |_____|       |_____|      |_____|      |_____|    
                                                                                 

        """
        self.options = ["1. Select own hero", "2. Start with default hero"]

    def display_menu(self):
        self.screen.fill((0, 0, 0))
        lines = self.ascii_logo.splitlines()
        y_offset = 50
        for line in lines:
            text_surface = self.font.render(line, True, (255, 255, 255))
            self.screen.blit(text_surface, (50, y_offset))
            y_offset += 30

        y_offset += 30
        for option in self.options:
            text_surface = self.font.render(option, True, (255, 255, 255))
            self.screen.blit(text_surface, (50, y_offset))
            y_offset += 30

        pygame.display.update()

    def get_user_choice(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        return 1
                    if event.key == pygame.K_2:
                        return 2

    def choose_hero_image(self):
        root = tk.Tk()
        root.withdraw()

        file_path = filedialog.askopenfilename(
            title="Select your Hero",
            filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")]
        )

        return file_path
