import keyboard

# macOS
print("Press a key (ESC to exit):")

def on_key_event(event):
    print(f"You pressed {event}")
    if event.name == 'esc':
        keyboard.unhook_all()

keyboard.hook(on_key_event)
keyboard.wait('esc')

# Windows
# def afficher_touche(evenement):
#     print(f"Touche pressée: {evenement.name} - ID: {evenement.scan_code}")

# keyboard.hook(afficher_touche)
# keyboard.wait('esc')  # Utilisez la touche 'esc' pour sortir du programme