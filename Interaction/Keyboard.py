"""
This class will handle the interaction with the keyboard.
Mainly space for the next step, backspace for the previous step and enter to generate a new tree.
"""


import pygame


class Keyboard:
    def __init__(self):
        """
        Keycodes:
        1   30      q   20      a   4       z   29
        2   31      w   26      s   22      x   27
        3   32      e   8       d   7       c   6
        4   33      r   21      f   9       v   25
        5   34      t   23      g   10      b   5
        6   35      y   28      h   11      n   17
        7   36      u   24      j   13      m   16
        8   37      i   12      k   14      ,   54
        9   38      o   18      l   15      .   55
        0   39      p   19      ;   51      /   56
        -   45      +   46      '   52

        space   44  backspace 42    enter 40
        """
        pass

    def return_key(self):
        pressed_keys = pygame.key.get_pressed()
        active_keys = set(())

        for key_constant, pressed in enumerate(pressed_keys):
            if pressed:
                active_keys.add(key_constant)
        return active_keys
