import keyboard

print("Press a key (ESC to exit):")

def on_key_event(event):
    print(f"You pressed {event}")
    if event.name == 'esc':
        keyboard.unhook_all()

keyboard.hook(on_key_event)
keyboard.wait('esc')
