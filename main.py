import pygame
import os


width, height = 700, 500
ship_width, ship_height = 100, 95

window = pygame.display.set_mode((width, height))

# images load here
background_image = pygame.image.load(
    os.path.join('assets', 'background.png'))

# spaceships image here
player_one_ship_image = pygame.image.load(
    os.path.join('assets', 'player_one_ship.png'))
player_two_ship_image = pygame.image.load(
    os.path.join('assets', 'player_two_ship.png'))

# resided spaceship
player_one_ship = pygame.transform.scale(
    player_one_ship_image, (ship_width, ship_height))
player_two_ship = pygame.transform.rotate(pygame.transform.scale(
    player_two_ship_image, (ship_width, ship_height)), 180)


def screen(player_one, player_two, player_one_bullets, player_two_bullets):
    window.blit(background_image, (0, 0))
    window.blit(player_one_ship, (player_one.x, player_one.y))
    window.blit(player_two_ship, (player_two.x, player_two.y))

    for bullet in player_one_bullets:
        pygame.draw.rect(window, (255, 0, 0), bullet)
    for bullet in player_two_bullets:
        pygame.draw.rect(window, (255, 255, 255), bullet)

    pygame.display.update()


def player_one_movement(pressed, player_one):
    if pressed[pygame.K_a]:
        player_one.x -= 5
    elif pressed[pygame.K_d]:
        player_one.x += 5
    elif pressed[pygame.K_w]:
        player_one.y -= 5
    elif pressed[pygame.K_s]:
        player_one.y += 5


def player_two_movement(pressed, player_two):
    if pressed[pygame.K_j]:
        player_two.x -= 5
    elif pressed[pygame.K_l]:
        player_two.x += 5
    elif pressed[pygame.K_i]:
        player_two.y -= 5
    elif pressed[pygame.K_k]:
        player_two.y += 5


def bullets(player_one_bullets, player_one, player_two_bullets, player_two):
    for bullet in player_one_bullets:
        bullet.x += 5

    for bullet in player_two_bullets:
        bullet.x -= 5


def main_window():
    player_one = pygame.Rect(10, 230, ship_width, ship_height)
    player_two = pygame.Rect(580, 230, ship_width, ship_height)

    player_one_bullets = []
    player_two_bullets = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)  # 60 fps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # firing action
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    bullet = pygame.Rect(
                        player_one.x + player_one.width, player_one.y + player_one.height // 2 - 2, 10, 5
                    )
                    player_one_bullets.append(bullet)

                if event.key == pygame.K_p:
                    bullet = pygame.Rect(
                        player_two.x, player_two.y + player_two.height // 2, 10, 5
                    )
                    player_two_bullets.append(bullet)

            # conditional main screen
        pressed = pygame.key.get_pressed()
        player_one_movement(pressed, player_one)
        player_two_movement(pressed, player_two)
        bullets(player_one_bullets, player_one, player_two_bullets, player_two)
        screen(player_one, player_two, player_one_bullets, player_two_bullets)

    pygame.quit()


if __name__ == "__main__":
    main_window()
