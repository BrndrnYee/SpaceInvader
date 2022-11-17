import pygame


class Enemy:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.image = pygame.Surface(self.rect.size)
        self.image.fill(pygame.Color((255, 125, 64)))

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Formation:
    def __init__(self, x, y, n):
        self.enemies = []
        self.x = x
        self.y = y
        self.gap = 60 - 50
        for i in range(n):
            enemy = Enemy(self.x + (50 + self.gap) * i, self.y)
            self.enemies.append(enemy)
        self.rect = pygame.Rect(
            self.x,
            self.y,
            self.enemies[0].rect.width * len(self.enemies) + self.gap * (len(self.enemies) - 1),
            self.enemies[0].rect.height)

    def hitBy(self, bullet):
        if bullet.rect.colliderect(self.rect):
            for enemy in self.enemies:
                if bullet.rect.colliderect(enemy.rect):
                    # todo deal damage
                    return True
        return False

    def update(self):
        pass

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
        pygame.draw.rect(
            screen,
            pygame.Color("green"),
            self.rect,
            width=1
        )
