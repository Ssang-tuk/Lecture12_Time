from pico2d import load_image, get_time, load_font
import game_world
import game_framework
from state_machine import StateMachine

class Bird:
    image = None

    def __init__(self):
        self.x = 0
        self.y = 500
        self.image = load_image('bird_animation.png')
        pass

    def draw(self):
        pass

    def do(self):
        pass

    def update(self):
        pass

