# pyfluffy: a pygame framework

## How to use it?

We just gonna see how to implement basic player movement and window

`It's gonna be short and simple!!`

```python
from pyfluffy import *

window = init_window("test", 800, 600)
player = init_rect(10, 10, 100, 100)

while program_alive():
    clear_screen(window, (255, 255, 255))

    move(player, (
        (get_action_strength_input("right") - get_action_strength_input("left")) * 2,
        (get_action_strength_input("down") - get_action_strength_input("up")) * 2 
        ))

    draw_rect(window, (0, 0, 0), player)

    update_screen()

```

## What else you can do?

It also has physics layer to interact with different objects in the world

Let see how that works in our demo.


* First we need another object to interact with so i'm going to introduce `platform`.
* `set_phyics_layer()` it's a function that takes two arguments, one is the object and then the list of object it wants to interact with.

```python
from pyfluffy import *

window = init_window("test", 800, 600)

player = init_rect(10, 10, 100, 100)
platform = init_rect(10, 400, 500, 50)

set_phyics_layer(player, [platform])

while program_alive():
    clear_screen(window, (255, 255, 255))

    move(player, (
        (get_action_strength_input("right") - get_action_strength_input("left")) * 2,
        (get_action_strength_input("down") - get_action_strength_input("up")) * 2 
        ))

    draw_rect(window, (0, 0, 0), player)
    draw_rect(window, (0, 0, 0), platform)

    update_screen()
```


# TODO
- [x] Window
- [x] Rects
- [x] Rendering
- [x] Movement
- [x] Basic Collision
- [ ] AABB Collision
