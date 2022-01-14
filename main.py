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

fps = 30
array_len = 100

clock = pygame.time.Clock()

pygame.init()
pygame.font.init() 
myfont = pygame.font.SysFont('Calibri', 30)

bar_len = 30

size = width, height = 1000, 500 + bar_len
black = 0, 0, 0
white = 255, 255, 255
green = 0, 255, 0
red = 255, 0, 0
purple = 255, 0, 255

screen = pygame.display.set_mode(size)

bogo_image = pygame.image.load("images/Bogo.jpg").convert_alpha()
quick_image = pygame.image.load("images/quick.jpg").convert_alpha()
bubble_image = pygame.image.load("images/Bubble.jpg").convert_alpha()
count_image = pygame.image.load("images/Count.jpg").convert_alpha()


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

restart("quick")

class Button():
    def __init__(self, x, y, image, alg):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.alg = alg

    def draw(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                restart(self.alg)

        screen.blit(self.image, (self.rect.x, self.rect.y))

    

quick_button  = Button(10, height - bar_len, quick_image, "quick")
count_button  = Button(120, height - bar_len, count_image, "counting")
bogo_button   = Button(340, height - bar_len, bogo_image, "bogo")
bubble_button = Button(230, height - bar_len, bubble_image, "bubble")

120, height - bar_len

buttons = [quick_button, count_button, bubble_button, bogo_button]

current_alg = "quick"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                array_len += 1
                restart(current_alg)
            elif event.key == pygame.K_DOWN:
                array_len -= 1
                restart(current_alg)
            elif event.key == pygame.K_RIGHT:
                fps += 1
            elif event.key == pygame.K_LEFT:
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
        h = (height - bar_len) / max(array) * num
        x = width / len(output) * i
        y = height - h - bar_len
        color = white if i > green_index else green
        if i == changed: color = red
        if i == other_changed: color = green

        pygame.draw.rect(screen, color, pygame.Rect(x, y, w, h))

    current_array_len = myfont.render("Number of elements: " + str(array_len), False, white)
    screen.blit(current_array_len, (0, 40))

    for button in buttons:
        button.draw()

    clock.tick(fps)
  
    pygame.display.flip()