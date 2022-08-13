# import

import pygame
import sys
from pygame.locals import *


# constants
true = True; false = False; nil = None

fluffy_alive = true

rect_id = 0; phy_mask = {}

# input keys
DEFAULT_KEYS = {
            "right": {
                    "keystrokes": [K_RIGHT, K_d],
                    "keystrength": 1
                },
            "left": {
                    "keystrokes": [K_LEFT, K_a],
                    "keystrength": 1
                },
            "down": {
                    "keystrokes": [K_DOWN, K_s],
                    "keystrength": 1
                },
            "up": {
                    "keystrokes": [K_UP, K_w],
                    "keystrength": 1
                }
        }

input_keys = {}


#############################################
#               Basic setup                 #
#############################################

def init_window(title, width, height):
    pygame.init()

    window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    pygame.display.set_caption(title)

    return window

def clear_screen(window, color): return window.fill(color)

def update_screen():
    global fluffy_alive

    # check if user wants to quit the application
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fluffy_alive = false

    update = pygame.display.update()
    return update

def program_alive(): return fluffy_alive


#############################################
#               Basic Input                 #
#############################################

def set_input_keys(name, keylist):
    to_set = {
                    "keystrokes": keylist,
                    "keystrength": 1
            }

    if name not in input_keys.get_keys(): input_keys[name] = to_set
    else: print("input key %s already set", name)

def get_input_keys(): return input_keys

def get_default_keys(): return DEFAULT_KEYS

def is_key_pressed_input(key):
    get_pressed_keys = pygame.key.get_pressed()

    if len(input_keys) > 0:
        for keystroke in input_keys[key]["keystrokes"]:
            if get_pressed_keys[keystroke]: return true 

    for keystroke in DEFAULT_KEYS[key]["keystrokes"]:
        if get_pressed_keys[keystroke]: return true 

    return false

def get_action_strength_input(key):
    get_pressed_keys = pygame.key.get_pressed()
    actionStrength = 0

    if len(input_keys) > 0:
        for keystroke in input_keys[key]["keystrokes"]:
            if get_pressed_keys[keystroke]: actionStrength = input_keys[key]["keystrength"]

    for keystroke in DEFAULT_KEYS[key]["keystrokes"]:
        if get_pressed_keys[keystroke]: actionStrength = DEFAULT_KEYS[key]["keystrength"]

    return actionStrength


#############################################
#            Rects and Rendering            #
#############################################

def get_rect_id():
    global rect_id
    rect_id += 1; return rect_id

def init_rect(x, y, w, h): return (pygame.Rect(x, y, w, h), get_rect_id())

def draw_rect(window, color, rect): return pygame.draw.rect(window, color, rect[0])


#############################################
#           Physics and Movement            #
#############################################

def set_phyics_layer(rect, mask_layer):
    global phy_mask
    phy_mask[rect[1]] = mask_layer

def move(rect, movement):
    res = basic_collision_testing(rect, movement)

def basic_collision_testing(rect, movement):
    result = [false, false, false, false]
    top = 0; bottom = 1; left = 2; right = 3

    col_lvl = 5
    a = rect[0]; mask = rect[1]

    rect[0].x += movement[0]
    rect[0].y += movement[1]

    if mask in phy_mask.keys():
        col = [i for i in phy_mask[mask] if i[0].colliderect(a)]


        for test_col_rect in col:
            b = test_col_rect[0]

            if abs(b.left - a.right) < col_lvl and movement[0] > 0:
                a.right = b.left + 1; result[right] = true

            if abs(b.right - a.left) < col_lvl and movement[0] < 0:
                a.left = b.right + 1; result[left] = true

            if abs(b.top - a.bottom) < col_lvl and movement[1] > 0:
                a.bottom = b.top + 1; result[bottom] = true

            if abs(b.bottom - a.top) < col_lvl and movement[1] < 0:
                a.top = b.bottom + 1; result[top] = true

    return result

def AABB(rect, movement):
    # FIXME: not implemented yet

    result = [false, false, false, false] # top, bottom, left, right
    top = 0; bottom = 1; left = 2; right = 3
    col_lvl = 5

    if rect[1] in phy_mask.keys():
        col = phy_mask[rect[1]]

        for obj in col:
            # TODO: return list of sides
            a = obj[0]; b = rect[0]
            AABB_RESULT = a.x < b.x + b.width and a.x + a.width > b.x and a.y < b.y + b.height and a.y + a.height > b.y

    return result
