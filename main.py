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

if len(sys.argv) < 2:
    raise NameError("Usage: python main.py <sorting algorithm>")

implemented_algs = ["quick", "counting", "bubble", "bogo"]
if sys.argv[1] not in implemented_algs:
    raise NameError(f"Algorithm Error: {sys.argv[1]} not in implemented algorithms.")

fps = 100
array_len = 1000

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

current_alg = sys.argv[1]

prev_time = time.time()

def restart(sort_algo):
    global array
    array = [i + 1 for i in range(array_len)]
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

restart(current_alg)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and array_len <= width:
                array_len += 5
                restart(current_alg)
            elif event.key == pygame.K_DOWN and array_len > 5:
                array_len -= 5
                restart(current_alg)
            elif event.key == pygame.K_RIGHT:
                fps += 1
            elif event.key == pygame.K_LEFT and fps > 1:
                fps -= 1
                

    now = time.time()
    dt = now - prev_time
    prev_time = now

    screen.fill(black)
    if output == sorted(array): is_sorted = True
    try:
        if not is_sorted: output, changed, other_changed = next(sort_gen)
        else: is_sorted, green_index, changed = True, green_index + 100 * dt, -1 
    except:
        is_sorted = True

    fps_surface = myfont.render("FPS: " + str(int(clock.get_fps())), False, white)
    screen.blit(fps_surface, (0, 0))




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

    current_array_len = myfont.render("Number of elements: " + str(array_len), False, white)
    screen.blit(current_array_len, (0, 40))
    current_alg_text = myfont.render("Current Algorithm: " + current_alg.capitalize(), False, white)
    screen.blit(current_alg_text, (0, 80))

    clock.tick(fps)
  
    pygame.display.flip()