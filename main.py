import pygame
pygame.init()

from scene_manager import SceneManager
from titleScene import TitleScene



screen = pygame.display.set_mode((525, 900))
pygame.display.set_caption("Space Invader")
clock = pygame.time.Clock()
player_hitbox = pygame.Rect(175, 340, 40, 40)
player_image = pygame.Surface((40, 40))
player_image.fill((0, 0, 255))

scene_manager = SceneManager(initial_scene=TitleScene())

while True:
    # event handling
    if pygame.event.get(eventtype=pygame.QUIT):
        pygame.quit()

    # game logic
    scene_manager.current_scene.handle_events(pygame.event.get())
    scene_manager.current_scene.update()
    scene_manager.current_scene.render(screen)

    pygame.display.flip()
    clock.tick(60)
