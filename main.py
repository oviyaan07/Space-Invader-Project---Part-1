import pygame
import random

pygame.init()

screen_width = 800
screen_height = 600

score=0

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invader")

bg = pygame.image.load("space bg.jpg")
aim = pygame.image.load("alien-ship.png")
rocket = pygame.image.load("rocket.png")

bg = pygame.transform.scale(bg, (screen_width, screen_height))
rocket = pygame.transform.scale(rocket, (60, 60))
aim = pygame.transform.scale(aim, (60, 60))

rocket_rect = rocket.get_rect()
rocket_rect.midbottom = (screen_width // 2, screen_height - 30)

aim_rect = aim.get_rect()
aim_rect.topleft = (random.randint(0, screen_width - aim_rect.width), 0)

bs=7
bullets=[]
bw=5
bh=10

rs = 5  # rocket speed
al = 3  # aim (alien) speed

font=pygame.font.SysFont(None,35)

running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rocket_rect.x -= rs
    if keys[pygame.K_RIGHT]:
        rocket_rect.x += rs
    if keys[pygame.K_SPACE]:
        # Fire a bullet from top of the rocket
        if len(bullets) < 5:  # Limit number of bullets on screen
            bullet_rect = pygame.Rect(rocket_rect.centerx - 2, rocket_rect.top - 10, 4, 10)
            bullets.append(bullet_rect)

    # Clamp rocket within screen bounds
    rocket_rect.x = max(0, min(rocket_rect.x, screen_width - rocket_rect.width))

    
    aim_rect.y += al
    if aim_rect.top > screen_height:
        aim_rect.topleft = (random.randint(0, screen_width - aim_rect.width), 0)

    for bullet in bullets:
        bullet.y=bullet.y-bs
    bullets=[b for b in bullets if b.bottom>0]
    for bullet in bullets:
        if bullet.colliderect(aim_rect):
            score=score+1
            bullets.remove(bullet)
            aim_rect.topleft = (random.randint(0, screen_width - aim_rect.width), 0)
            break

    screen.blit(bg, (0, 0))
    screen.blit(rocket, rocket_rect)
    screen.blit(aim, aim_rect)
    for bullet in bullets:
        pygame.draw.rect(screen,(255,255,0),bullet)
    
    sc=font.render("SCORE "+str(score),True,(255,231,157))
    screen.blit(sc,(10,10))

    pygame.display.flip()

pygame.quit()