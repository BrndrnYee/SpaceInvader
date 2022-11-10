import pygame

class Enemy:
    def __init__(self):
        self.rect = pygame.Rect(525/2, 75, 50, 50)
        self.image = pygame.Surface(self.rect.size)
        self.image.fill(pygame.Color((255, 125, 64)))

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Formation:
    def __init__(self, x, y, n):
        self.enemies = []
        # todo: save x and y
        for i in range(n):
            # todo: customize enemy position
            enemy = Enemy()
            self.enemies.append(enemy)

    def update(self):
        pass

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
        pygame.draw.rect(screen, pygame.Color("green"), pygame.Rect(x, y, self.enemies[0].rect.width * len(self.enemies), self.enemies[0].rect.height * len(self.enemies)), width = 1)
