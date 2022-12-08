import pygame

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y), (50, 50))
        self.image = pygame.image.load("images/player_ship.webp")
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
        self.x_vel = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def handle_events(self, events):
        pass

    def update(self):
        keymap = pygame.key.get_pressed()
        if keymap[pygame.K_LEFT]:
            self.x_vel -= 1
        if keymap[pygame.K_RIGHT]:
            self.x_vel += 1
        self.rect.x += self.x_vel
        self.x_vel *= 0.92
