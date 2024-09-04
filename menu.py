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
        option_rects = []
        y_offset = 50 + len(self.ascii_logo.splitlines()) * 30 + 30
        for _ in self.options:
            rect = pygame.Rect(50, y_offset, 300, 30)
            option_rects.append(rect)
            y_offset += 30

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        return 1
                    if event.key == pygame.K_2:
                        return 2
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    for idx, rect in enumerate(option_rects):
                        if rect.collidepoint(mouse_pos):
                            return idx + 1

    def choose_hero_image(self):
        root = tk.Tk()
        root.withdraw()

        file_path = filedialog.askopenfilename(
            title="Select your Hero",
            filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")]
        )

        return file_path
