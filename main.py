import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
import sys
import random
import time

import countingSort
import bubbleSort
import bogoSort
import quickSort


print("bogo     - Bogo Sort.")
print("bubble   - Bubble Sort.")
print("counting - Counting Sort.")
print("quick    - Quick Sort")
sort_algo = input("What Sorting Algorithm do you want: ")
fps = int(input("What do you want the FPS (Frames Per Second) to be: "))
array_len = int(input("How many items do you want in the array (DO NOT GO OVER 1000): "))

clock = pygame.time.Clock()

pygame.init()
pygame.font.init() 
myfont = pygame.font.SysFont('Calibri', 30)

size = width, height = 1000, 500
black = 0, 0, 0
white = 255, 255, 255
green = 0, 255, 0
red = 255, 0, 0
purple = 255, 0, 255

screen = pygame.display.set_mode(size)

prev_time = time.time()

def restart():
    global array
    array = [i for i in range(array_len)]
    random.shuffle(array)
    global output
    output = array.copy()

    global sort_gen
    if   sort_algo == "bogo": sort_gen = bogoSort.bogoSort(array)
    elif sort_algo == "bubble": sort_gen = bubbleSort.bubbleSort(array)
    elif sort_algo == "counting": sort_gen = countingSort.countingSort(max(array) + 1, array)
    elif sort_algo == "quick": sort_gen = quickSort.quickSort(array, 0, len(array) - 1)

    global operated
    operated = 0
    global is_sorted
    is_sorted = False
    global green_index
    green_index = -1
    global changed
    changed = -2
    global other_changed
    other_changed = -2
restart()


while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN: restart()

    now = time.time()
    dt = now - prev_time
    prev_time = now

    screen.fill(black)

    text_surface = myfont.render("FPS: " + str(int(clock.get_fps())), False, white)
    screen.blit(text_surface, (0, 0))

    if output != sorted(array): output, changed, other_changed = next(sort_gen)
    else: is_sorted, green_index, changed = True, green_index + 100 * dt, -1 

    if green_index > len(output): green_index = len(output)

    for i, num in enumerate(output):
        w = width / len(output)
        h = height / max(array) * num
        x = width / len(output) * i
        y = height - h
        color = white if i > green_index else green
        if i == changed: color = red
        if i == other_changed: color = green

        pygame.draw.rect(screen, color, pygame.Rect(x, y, w, h))
    


    clock.tick(fps)
  
    pygame.display.flip()