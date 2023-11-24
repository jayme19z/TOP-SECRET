'''
Create a simple clock application (only with minutes and seconds) which is synchronized with system clock. 
Use Mickey's right hand as minutes arrow and left - as seconds. For moving Mickey's hands you can use: 
pygame.transform.rotate more explanation: https://stackoverflow.com/a/54714144
'''
import pygame
from datetime import datetime

pygame.init()

size = width, height = 800, 800
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mickey Mouse Clock")

main_clock = pygame.image.load('C:/Users/kozha/OneDrive/Рабочий стол/Lab9/main-clock.png')
main_clock = pygame.transform.scale(main_clock, (600, 600))
rect_main_clock = main_clock.get_rect()
rect_main_clock.center = (width // 2, height // 2)

left_hand = pygame.image.load('C:/Users/kozha/OneDrive/Рабочий стол/Lab9/left-hand.png')
left_hand = pygame.transform.scale(left_hand, (360, 90))
rect_left_hand = left_hand.get_rect()
rect_left_hand.center = (width - 365, height - 420)

right_hand = pygame.image.load('C:/Users/kozha/OneDrive/Рабочий стол/Lab9/right-hand.png')
right_hand = pygame.transform.scale(right_hand, (320, 80))
rect_right_hand = right_hand.get_rect()
rect_right_hand.center = (width - 465, height - 420)

clock = pygame.time.Clock()
FPS = 60

def left_hand_angle():
    return (90 - 6 * datetime.now().second) % 360

def right_hand_angle():
    return (90 - 6 * datetime.now().minute) % 360

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill((255, 255, 255))

    rotated_left_hand = pygame.transform.rotate(left_hand, left_hand_angle())
    rect_rotated_left_hand = rotated_left_hand.get_rect()
    rect_rotated_left_hand.center = rect_left_hand.center

    rotated_right_hand = pygame.transform.rotate(right_hand, right_hand_angle())
    rect_rotated_right_hand = rotated_right_hand.get_rect()
    rect_rotated_right_hand.center = rect_right_hand.center

    screen.blit(main_clock, rect_main_clock)
    screen.blit(rotated_left_hand, rect_rotated_left_hand)
    screen.blit(rotated_right_hand, rect_rotated_right_hand)

    pygame.display.update()
    clock.tick(FPS)
