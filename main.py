import pygame
import random

pygame.init()

screen_width=800
screen_height=600

screen=pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("space invader")

bg=pygame.image.load("space bg.jpg")
aim=pygame.image.load("alien-ship.png")
rocket=pygame.image.load("rocket.png")

bg=pygame.transform.scale(bg,(screen_width,screen_height))
rocket=pygame.transform.scale(rocket,(80,80))
aim=pygame.transform.scale(aim,(60,60))

rocket_rect=rocket.get_rect()
rocket_rect.midbottom=(screen_width//2,screen_height-30)

aim_rect=aim.get_rect()
aim_rect.topleft=(random.randint(0,800-aim_rect.width),0)

rs=5
al=3

running=True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    
    keys=pygame.key.get_pressed()
    if keys [pygame.K_LEFT]:
        rocket_rect.x=rocket_rect.x-rs
    if keys [pygame.K_RIGHT]:
        rocket_rect.x=rocket_rect.x+rs

    rocket_rect.left=max(0,rocket_rect.left)
    rocket_rect.left=min(screen_width,rocket_rect.right)

    screen.blit(bg,(0,0))
    screen.blit(rocket,rocket_rect)
    screen.blit(aim,aim_rect)

    pygame.display.flip()

pygame.quit()