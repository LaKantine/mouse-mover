import pyautogui
import random
import time
from pynput import keyboard
import threading
import sys

running = True

def on_press(key):
    global running
    if key == keyboard.Key.space:
        running = False
        sys.exit()

listener = keyboard.Listener(on_press=on_press)
listener.start()

while running:
    x = random.randint(-20, 20)
    y = random.randint(-20, 20)
    pyautogui.moveRel(x, y, duration=0.2)
    time.sleep(5)
