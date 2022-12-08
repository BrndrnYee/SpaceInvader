import pygame

bullet_image = pygame.image.load("images/bullet.png")
class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y), (10, 10))
        # self.image = pygame.Surface(self.rect.size)
        self.image = pygame.transform.scale(bullet_image, (self.rect.w, self.rect.h))
        self.image = pygame.transform.flip(self.image, False, True)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def handle_events(self, events):
        pass

    def update(self):
        self.rect.y -= 5

