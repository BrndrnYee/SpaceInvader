import pygame
import time
import random
from bullet import Bullet

enemy_image = pygame.image.load("images/enemy.png")
class Enemy:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        # self.image = pygame.Surface(self.rect.size)
        # self.image.fill(pygame.Color((255, 125, 64)))
        self.image = pygame.transform.scale(enemy_image, (self.rect.w, self.rect.h))
        self.health = 1
        self.reload_time_range = [1, 5]
        self.next_fire_time = time.time() + random.randint(*self.reload_time_range)
        self.bullet = None

    def update(self):
        if time.time() > self.next_fire_time:
            self.bullet = Bullet(self.rect.centerx, self.rect.centery, True)
            self.next_fire_time = time.time() + random.randint(*self.reload_time_range)

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
        self.moving_right = True

    def hitBy(self, bullet):
        if bullet.going_down == False and bullet.rect.colliderect(self.rect):
            for enemy in self.enemies:
                if bullet.rect.colliderect(enemy.rect):
                    enemy.health -= 1
                    if enemy.health <= 0:
                        self.enemies.remove(enemy)
                    return True
        return False

    def update(self):
        if self.moving_right:
            self.rect.x += 1
            for enemy in self.enemies:
                enemy.rect.x += 1
        else:
            self.rect.x -= 1
            for enemy in self.enemies:
                enemy.rect.x -= 1
        if self.rect.right > 500:
            self.moving_right = False
            self.rect.right = 500
            self.rect.y += 10
            for enemy in self.enemies:
                enemy.rect.y += 10
        if self.rect.left < 25:
            self.moving_right = True
            self.rect.left = 25
            self.rect.y += 10
            for enemy in self.enemies:
                enemy.rect.y += 10
        for enemy in self.enemies:
            enemy.update()

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
        pygame.draw.rect(
            screen,
            pygame.Color("green"),
            self.rect,
            width=1
        )
