import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
import sys
import random
import time

import algorithms.countingSort as countingSort
import algorithms.bubbleSort as bubbleSort
import algorithms.bogoSort as bogoSort
import algorithms.quickSort as quickSort
import algorithms.mergeSort as mergeSort
import algorithms.combSort as combSort
import algorithms.shellSort as shellSort
import algorithms.stoogeSort as stoogeSort
import algorithms.selectionSort as selectionSort
import algorithms.gnomeSort as gnomeSort
import algorithms.cocktailSort as cocktailSort

if len(sys.argv) < 2:
    raise NameError("Usage: python main.py <sorting algorithm>")

implemented_algs = ["quick", "counting", "bubble", "bogo", "merge", "comb", "shell", "stooge", "selection", "gnome", "cocktail"]
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
    global comparisons
    comparisons = 0
    global swaps
    swaps = 0

    global sort_gen
    if   sort_algo == "bogo": sort_gen = bogoSort.bogoSort(array)
    elif sort_algo == "bubble": sort_gen = bubbleSort.bubbleSort(array)
    elif sort_algo == "counting": sort_gen = countingSort.countingSort(max(array) + 1, array)
    elif sort_algo == "quick": sort_gen = quickSort.quickSort(array, 0, len(array) - 1)
    elif sort_algo == "merge": sort_gen = mergeSort.mergeSort(array, 0, len(array) - 1)
    elif sort_algo == "comb": sort_gen = combSort.combSort(array)
    elif sort_algo == "shell": sort_gen = shellSort.shellSort(array)
    elif sort_algo == "stooge": sort_gen = stoogeSort.stoogeSort(array)
    elif sort_algo == "selection": sort_gen = selectionSort.selectionSort(array)
    elif sort_algo == "gnome": sort_gen = gnomeSort.gnomeSort(array)
    elif sort_algo == "cocktail": sort_gen = cocktailSort.cocktailSort(array)




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
            if event.key == pygame.K_UP and array_len < width:
                array_len += 100
                restart(current_alg)
            elif event.key == pygame.K_DOWN and array_len > 100:
                array_len -= 100
                restart(current_alg)
            elif event.key == pygame.K_RIGHT:
                fps += 10
            elif event.key == pygame.K_LEFT and fps > 10:
                fps -= 10
                

    now = time.time()
    dt = now - prev_time
    prev_time = now

    screen.fill(black)
    if output == sorted(array): is_sorted = True
    prev_comparisons = comparisons
    prev_swaps = swaps
    # try:
    if not is_sorted:
        output, changed, other_changed, comparisons, swaps = next(sort_gen)
        comparisons = comparisons + prev_comparisons
        swaps = swaps + prev_swaps
    else: is_sorted, green_index, changed = True, green_index + 100 * dt, -1 
    # except:
    #     is_sorted = True

    fps_surface = myfont.render("COMPARISONS: " + str(comparisons), False, white)
    screen.blit(fps_surface, (0, 0))
    fps_surface = myfont.render("SWAPS: " + str(swaps), False, white)
    screen.blit(fps_surface, (0, 40))




    if green_index > len(output): green_index = len(output)

    for i, num in enumerate(output):
        w = width / len(output)
        h = height / max(array) * num
        x = width / len(output) * i
        y = height - h
        if i == changed and not is_sorted: color = red
        elif (i == other_changed and not is_sorted) or i <= green_index: color = green
        else: color = white


        pygame.draw.rect(screen, color, pygame.Rect(x, y, w, h))

    clock.tick(fps)
  
    pygame.display.flip()