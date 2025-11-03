from pico2d import load_image, get_time, load_font
import random
import game_world
import game_framework
from state_machine import StateMachine

class Bird:
    image = None

    def __init__(self):
        self.x = random.randint(100, 500)
        self.y = random.randint(300, 500)
        self.dir = 1
        self.image = load_image('bird_animation.png')
        pass

    def draw(self):
        pass

    def do(self):
        pass

    def update(self):
        pass

