import sys
import pygame
import tkinter as tk
from tkinter import filedialog


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(pygame.font.match_font('consolas', bold=True), 24)
        self.ascii_logo = """
 _______  _______          _________ _______  _______ 
(  ____ \/ ___   )|\     /|\__   __/(  ____ \(  ____ )
| (    \/\/   )  || )   ( |   ) (   | (    \/| (    )|
| (_____     /   )| |   | |   | |   | (__    | (____)|
(_____  )   /   / | |   | |   | |   |  __)   |     __)
      ) |  /   /  | |   | |   | |   | (      | (\ (   
/\____) | /   (_/\| (___) |   | |   | (____/\| ) \ \__
\_______)(_______/(_______)   )_(   (_______/|/   \__/ 
        """
        self.ascii_start = """
    _________________________ _____________________
   /   _____/\__    ___/  _  \\______   \__    ___/
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
            text_surface = self.font.render(line, True, (255, 255, 255))
            self.screen.blit(text_surface, (50, y_offset))
            y_offset += 20

        y_offset += 20
        options_text = "Choose your Hero"
        text_surface = self.font.render(options_text, True, (139, 0, 0))
        self.screen.blit(text_surface, (50, y_offset))
        y_offset += 30
        for option in self.options:
            text_surface = self.font.render(option, True, (255, 255, 255))
            self.screen.blit(text_surface, (50, y_offset))
            y_offset += 20

        y_offset += 20
        difficulties_text = "Choose Difficulty"
        text_surface = self.font.render(difficulties_text, True, (139, 0, 0))
        self.screen.blit(text_surface, (50, y_offset))
        y_offset += 30
        for difficulty in self.difficulties:
            text_surface = self.font.render(difficulty, True, (255, 255, 255))
            self.screen.blit(text_surface, (50, y_offset))
            y_offset += 20

        y_offset += 1
        start_lines = self.ascii_start.splitlines()
        for start_line in start_lines:
            text_surface = self.font.render(start_line, True, (255, 255, 255))
            self.screen.blit(text_surface, (50, y_offset))
            y_offset += 20
        start_text = "Press SPACE to start"
        text_surface = self.font.render(start_text, True, (255, 0, 0))
        self.screen.blit(text_surface, (50, y_offset))

        pygame.display.update()

    def get_user_choice(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
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

    def choose_hero_image(self):
        root = tk.Tk()
        root.withdraw()

        file_path = filedialog.askopenfilename(
            title="Select your Hero",
            filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")]
        )

        return file_path
