#             - = Virtual Piano Controller = -
#                  - By Ben Griffiths - 
#      Takes a MIDI file and plays it through virtualpiano

import midi_tools.parse
import important.important_classes

important.important_classes.adjust_latency() # Get roblox tick time and adjust midi timings to match
path_to_midi_file = "E:\\Programming\\projects\\python\\virtualPianoController\\test_midis\\Alan_Walker_-_Faded.mid"
parsed_object = midi_tools.parse.parse_midi_file(path_to_midi_file)
midi_tools.parse.play_midi_file(parsed_object)