import pyautogui
import keyboard
import time
import json
import random

en_pause = False

def pause_unpause():
  global en_pause
  en_pause = not en_pause
  print("Paused" if en_pause else "Unpaused")

def clique_competence(x1, y1, x2, y2, nom_macro):
  global en_pause
  if en_pause:
    return
  
  x_init, y_init = pyautogui.position()
  
  x_click = random.uniform(x1, x2)
  y_click = random.uniform(y1, y2)
  
  pyautogui.click(x_click, y_click)
  
  print(f"{nom_macro} at ({x_click}, {y_click})")
  
  pyautogui.moveTo(x_init, y_init)

def charger_macros():
  with open('config.json', 'r') as file:
    config = json.load(file)
    for macro, details in config.items():
      x1, y1 = details['position']['top_left']
      x2, y2 = details['position']['bottom_right']
      
      def make_lambda(x1, y1, x2, y2, nom_macro):
        return lambda: clique_competence(x1, y1, x2, y2, nom_macro)
      
      keyboard.add_hotkey(details['key'], make_lambda(x1, y1, x2, y2, macro))

keyboard.add_hotkey('esc', pause_unpause)

charger_macros()

print("WasherAutoMacro Script starting... Press CTRL+C to stop.")
print("Press Escape to pause/unpause.")

try:
  while True:
    time.sleep(1)
except KeyboardInterrupt:
  print("Script off.")