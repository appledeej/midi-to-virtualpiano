from tkinter import Tk, Label, Button
from tkinter.filedialog import askopenfilename
import midi_tools.parse

global file
file = ""

global parsed_object
parsed_object = {}

def main():
    window = Tk()
    window.title("MIDI to VirtualPiano")
    window.geometry('450x200')
    lbl = Label(window, text="MIDI to VirtualPiano", font=("Arial Bold", 35))
    lbl.grid(column=0, row=0)

    copyrightm = Label(window, text="MIDI to VirtualPiano created by Ben Griffiths and released under GNU GPLv3.0.", font=("Arial Bold", 8))
    copyrightm.grid(column=0,row=8)

    info_msg = Label(window, text="")
    info_msg.grid(column=0, row=7)

    def setMsg(message):
        info_msg.configure(text=message)

    def playMidiFile():
        setMsg("Playing... Please switch to VirtualPiano window.")
        midi_tools.parse.play_midi_file(parsed_object)
        print("Done!")
        import sys
        sys.exit()

    playbtn = Button(window, text="Play MIDI file", command=playMidiFile, state="disabled")
    playbtn.grid(column=0, row=4)

    parsebtn = Button(window, text="Parse MIDI file", state="disabled")

    def ParseMidiFile():
        setMsg("Parsing...")
        global parsed_object
        parsebtn.configure(state="disabled", text="Parsing...")
        parsed_object = midi_tools.parse.parse_midi_file(file)
        parsebtn.configure(state="disabled", text="File Parsed")
        playbtn.configure(state="normal")
        setMsg("Parsed file. Ready to play")

    parsebtn.configure(text="Parse MIDI file", command=ParseMidiFile, state="disabled")
    parsebtn.grid(column=0, row=2)

    def promptFileOpen():
        global file
        setMsg("User choosing file.")
        name = askopenfilename(filetypes =(("MIDI File", ["*.mid", "*.midi"]),("All Filetypes","*.*")),
                            title = "Choose a MIDI file."
                            )
        if len(name) > 1:
            choosebtn.configure(state="disabled", text=name.split("/")[-1])
            parsebtn.configure(state="normal")
            file = name
            setMsg("Loaded file " + name.split("/")[-1])
        else:
            setMsg("Opening file failed.")

    choosebtn = Button(window, text="Select Midi File", command=promptFileOpen)
    choosebtn.grid(column=0, row=1)

    setMsg("Initialized.")

    window.mainloop()

