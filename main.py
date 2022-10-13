import pygame

pygame.init()

screen = pygame.display.set_mode((525, 900))
pygame.display.set_caption("Space Invader")
clock = pygame.time.Clock()
player_hitbox = pygame.Rect(175, 340, 40, 40)
player_image = pygame.Surface((40, 40))
player_image.fill((0, 0, 255))

while True:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_hitbox.center = screen.get_width() / 2, screen.get_height() / 2
            if event.key == pygame.K_UP:
                player_hitbox.y -= 50


    # game logic
    #player_hitbox.x += 2
    keymap = pygame.key.get_pressed()
    if keymap[pygame.K_DOWN]:
        player_hitbox.y += 50

    # drawing game
    screen.fill((255, 255, 255))
    screen.blit(player_image, player_hitbox)
    pygame.display.flip()
    clock.tick(60)
