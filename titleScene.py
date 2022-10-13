import pygame

title_font = pygame.font.Font("pixel_sans.ttf", 60)
title_font.bold = True

class TitleScene:
    def __init__(self):
        self.scene_manager = None

    def handle_events(self, events: list[pygame.event.Event]):
        pass

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
        screen.blit(title4, (screen.get_width() / 2 - title3.get_width() / 2+ 5, 115))
        screen.blit(title3, (screen.get_width()/2 - title3.get_width()/2, 120))
