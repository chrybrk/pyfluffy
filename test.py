# test program
from pyfluffy import *

window = init_window("test", 800, 600)

player = init_rect(10, 10, 100, 100)
platform = init_rect(10, 400, 500, 50)

set_phyics_layer(player, [platform])

while program_alive():
    clear_screen(window, (255, 255, 255))

    move(player, (
        (get_action_strength_input("right") - get_action_strength_input("left")),
        (get_action_strength_input("down") - get_action_strength_input("up")) 
        ))

    draw_rect(window, (0, 0, 0), player)
    draw_rect(window, (0, 0, 0), platform)

    update_screen()
