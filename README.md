# Virtual Piano Controller
### Plays midi files on virtualpiano.net

## Usage
 - Install dependencies: `pip install -r requirements.txt`
 - Run script: `python3 run.py`
 - Select MIDI file using dialogue, and press parse
 - Once parsing has completed, open [VirtualPiano](https://virtualpiano.net) in a browser tab
 - Press "Play" and focus on the virtualpiano window
 - Wait for the song to finish, or hit Ctrl-C in command prompt to stop

## Acknowledgements
This program has various dependencies, which you can read in requirements.txt, however, I've listed the main ones here:
 - [Mido](https://github.com/mido/mido) by mido
 - [Pyautogui](https://github.com/asweigart/pyautogui) by asweigart
 - [requests](https://github.com/kennethreitz/requests) by kennethreitz
 - [rollbar](https://github.com/rollbar/pyrollbar) by rollbar
 - [tkinter](https://github.com/python/cpython/tree/master/Lib/tkinter) by python
 - [time](https://github.com/python/cpython/blob/master/Modules/timemodule.c) by python
