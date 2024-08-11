This tool is designed as part of an internship task in Cyber Security at Prodigy InfoTech.

This project is a keylogger tool developed using Python. Once started, the tool logs all keystrokes, including special keys, and saves them to a log file with timestamps. The keystrokes are recorded in intervals, making it easier to track key events over time. The log file is saved in the same directory as the script.

Prerequisites
- pynput library - Used to capture keyboard input.

How It Works
- The program uses the pynput library to monitor and capture keyboard events.
- Keystrokes are stored in a list and logged in 30-second intervals.
- At the end of each interval, the keystrokes are written to a file along with the starting timestamp of that interval.
- The Esc key can be used to stop the keylogger.
