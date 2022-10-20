import pygame
import button
import sys
from game_scene import GameScene

title_font = pygame.font.Font("pixel_sans.ttf", 60)
title_font.bold = True

class TitleScene:
    def __init__(self):
        self.scene_manager = None

        def play_button_click():
            self.scene_manager.go_to(GameScene())

        self.play_button = button.Button("Play", (400, 720, 150, 75), text_font=pygame.font.Font("pixel_sans.ttf", 50), on_click_fn= play_button_click)
        self.quit_button = button.Button("Quit", (400, 720, 150, 75), text_font=pygame.font.Font("pixel_sans.ttf", 50), on_click_fn= lambda: sys.exit(0))


    def handle_events(self, events: list[pygame.event.Event]):
        self.play_button.handle_events(events)
        self.quit_button.handle_events(events)

    def update(self):
        pass

    def render(self, screen: pygame.Surface):
        screen.fill((0, 0, 0))
        title = title_font.render("Space", True, (255, 255, 0))
        title2 = title_font.render("Space", True, (255, 0 ,0))
        title3 = title_font.render("Invader", True, (255, 255, 0))
        title4 = title_font.render("Invader", True, (255, 0, 0))
        screen.blit(title2, (screen.get_width() / 2 - title.get_width() / 2 + 5, 45))
        screen.blit(title, (screen.get_width() / 2 - title.get_width() / 2, 50))
        screen.blit(title4, (screen.get_width() / 2 - title3.get_width() / 2 + 5, 115))
        screen.blit(title3, (screen.get_width()/2 - title3.get_width()/2, 120))

        self.play_button.rect.centerx = screen.get_width()/2
        self.play_button.rect.centery = screen.get_height()/2
        self.quit_button.rect.centerx = screen.get_width() / 2
        self.quit_button.rect.centery = screen.get_height() / 2 + 100
        screen.blit(self.play_button.render(), self.play_button.rect)
        screen.blit(self.quit_button.render(), self.quit_button.rect)
