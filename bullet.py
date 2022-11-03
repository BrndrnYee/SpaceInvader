import pygame

class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y), (5, 10))
        self.image = pygame.Surface(self.rect.size)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def handle_events(self, events):
        pass

    def update(self):
        self.rect.y -= 5

