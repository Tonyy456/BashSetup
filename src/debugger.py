# debugger.py
import os

class Debugger:
    def __init__(self):
        self.debug_counter = 0

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_red(self, msg):
        print(f"\033[0;31m{msg}\033[0m")

    def debug(self, msg):
        self.debug_counter += 1
        print(f"\033[0;31m{self.debug_counter}\033[0m > {msg}")


