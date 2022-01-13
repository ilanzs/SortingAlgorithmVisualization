import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
import sys
import countingSort
import random

pygame.init()
size = width, height = 1000, 500
black = 0, 0, 0
white = 255, 255, 255
green = 0, 255, 0

screen = pygame.display.set_mode(size)

array = [i for i in range(100)]
random.shuffle(array)
output = array.copy()
sort_gen = countingSort.countingSort(max(array) + 1, array)
operated = 0
is_sorted = False
green_index = -1

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
         if event.type == pygame.QUIT: sys.exit()
    screen.fill(black)

    for i, num in enumerate(output):
        w = width / len(output)
        h = height / max(array) * num
        x = width / len(output) * i
        y = height - h
        color = white if i > green_index else green

        pygame.draw.rect(screen, color, pygame.Rect(x, y, w, h))
    
    if output != sorted(array): output = next(sort_gen)
    else: is_sorted, green_index = True, green_index + 1 

    if green_index > len(output): green_index = len(output)

    clock.tick(60)
  
    pygame.display.flip()