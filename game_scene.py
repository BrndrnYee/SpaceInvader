import pygame
from player import Player
from bullet import Bullet
from enemy import Formation

class GameScene:
    def __init__(self):
        self.player = Player(525/2-25, 750)
        self.formation = Formation(50, 50, 5)
        self.bullets = []
    
    def handle_events(self, events: list[pygame.event.Event]):
        self.player.handle_events(events)
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bullets.append(Bullet(self.player.rect.centerx, 750))

    def update(self):
        self.player.update()
        if self.player.rect.right >= 525:
            self.player.rect.right = 525
        if self.player.rect.left <= 0:
            self.player.rect.left = 0
        for bullet in self.bullets:
            bullet.update()
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)
            if self.formation.hitBy(bullet):
                self.bullets.remove(bullet)



    def render(self, screen: pygame.Surface):
        screen.fill((0, 0, 255))
        self.player.draw(screen)
        for bullet in self.bullets:
            bullet.draw(screen)
        self.formation.draw(screen)
