# debugger.py
import os

debug_counter = 0

class TonyDebuggerHelperClass:
    def __init__(self):
        self.counter = 0

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_red(self, msg):
        print(f"\033[0;31m{msg}\033[0m")

    def debug(self, msg):
        self.counter += 1
        print(f"\033[0;31m{self.counter}\033[0m > {msg}")

debugger = TonyDebuggerHelperClass()
clear= debugger.clear
print_red = debugger.print_red
debug = debugger.debug




