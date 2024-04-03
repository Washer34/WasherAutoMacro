from pynput import mouse
import pyautogui

def on_click(x, y, button, pressed):
  if pressed:
    print(f"Cursor position: ({x}, {y})")

with mouse.Listener(on_click=on_click) as listener:
  listener.join() 