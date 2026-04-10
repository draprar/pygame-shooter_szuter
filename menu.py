import sys
import pygame
import tkinter as tk
from tkinter import filedialog
from constants import SCREEN_WIDTH


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(pygame.font.match_font('consolas', bold=True), 24)
        self.ascii_logo = r"""
 _______  _______          _________ _______  _______ 
(  ____ \/ ___   )|\     /|\__   __/(  ____ \(  ____ )
| (    \/\/   )  || )   ( |   ) (   | (    \/| (    )|
| (_____     /   )| |   | |   | |   | (__    | (____)|
(_____  )   /   / | |   | |   | |   |  __)   |     __)
      ) |  /   /  | |   | |   | |   | (      | (\ (   
/\____) | /   (_/\| (___) |   | |   | (____/\| ) \ \__
\_______)(_______/(_______)   )_(   (_______/|/   \__/ 
        """
        # raw string: \__ etc. are visual characters, not escape sequences
        # The single \______  on line 2 replaces the former \\ (double-backslash)
        self.ascii_start = r"""
    _________________________ _____________________
   /   _____/\__    ___/  _  \______   \__    ___/
   \_____  \   |    | /  /_\  \|       _/ |    |   
   /        \  |    |/    |    \    |   \ |    |   
  /_______  /  |____|\____|__  /____|_  / |____|   
          \/                 \/       \/           
        """
        self.options = ["1. Select own hero", "2. Start with default hero"]
        self.difficulties = ["E. Easy", "N. Normal", "H. Hard"]
        self.selected_option = None
        self.selected_difficulty = None

    def display_menu(self):
        self.screen.fill((0, 0, 0))
        lines = self.ascii_logo.splitlines()
        y_offset = 1
        for line in lines:
            text_surface = self.font.render(line, True, (153, 0, 0))
            self.screen.blit(text_surface, (50, y_offset))
            y_offset += 20

        y_offset += 20
        options_text = "Choose your Hero"
        text_surface = self.font.render(options_text, True, (0, 102, 0))
        self.screen.blit(text_surface, (50, y_offset))
        y_offset += 30
        for choice, option in enumerate(self.options):
            color = (0, 255, 0) if self.selected_option == choice + 1 else (217, 217, 217)
            text_surface = self.font.render(option, True, color)
            self.screen.blit(text_surface, (50, y_offset))
            y_offset += 20

        y_offset += 20
        difficulties_text = "Choose Difficulty"
        text_surface = self.font.render(difficulties_text, True, (0, 102, 0))
        self.screen.blit(text_surface, (50, y_offset))
        y_offset += 30
        for choice, difficulty in zip(['E', 'N', 'H'], self.difficulties):
            color = (0, 255, 0) if self.selected_difficulty == choice else (255, 255, 255)
            text_surface = self.font.render(difficulty, True, color)
            self.screen.blit(text_surface, (50, y_offset))
            y_offset += 20

        y_offset += 20
        # BUG FIX: render "Press SPACE" header first, then advance y before ASCII art
        start_text = "Press SPACE to start"
        text_surface = self.font.render(start_text, True, (0, 102, 0))
        x_center = (SCREEN_WIDTH - text_surface.get_width()) // 2
        self.screen.blit(text_surface, (x_center, y_offset))
        y_offset += 30

        for start_line in self.ascii_start.splitlines():
            text_surface = self.font.render(start_line, True, (217, 217, 217))
            self.screen.blit(text_surface, (50, y_offset))
            y_offset += 20

        pygame.display.update()

    def get_user_choice(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.selected_option = 1
                    if event.key == pygame.K_2:
                        self.selected_option = 2
                    if event.key == pygame.K_e:
                        self.selected_difficulty = 'E'
                    if event.key == pygame.K_n:
                        self.selected_difficulty = 'N'
                    if event.key == pygame.K_h:
                        self.selected_difficulty = 'H'
                    if event.key == pygame.K_SPACE:
                        if self.selected_option and self.selected_difficulty:
                            return self.selected_option, self.selected_difficulty
                        else:
                            return 2, 'E'

            self.display_menu()

    def choose_hero_image(self):
        root = tk.Tk()
        root.withdraw()
        try:
            file_path = filedialog.askopenfilename(
                title="Select your Hero",
                filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")]
            )
        finally:
            root.destroy()
        return file_path
