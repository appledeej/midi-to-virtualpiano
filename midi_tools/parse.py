import mido
import time
import log
import pyautogui
from threading import Thread

midi_defenitions = {
    36: '1',
    37: '!',
    38: '2',
    39: '"',
    40: '3',
    41: '4',
    42: '$',
    43: '5',
    44: '%',
    45: '6',
    46: '^',
    47: '7',
    48: '8',
    49: '*',
    50: '9',
    51: '(',
    52: '0',
    53: 'q',
    54: 'Q',
    55: 'w',
    56: 'W',
    57: 'e',
    58: 'E',
    59: 'r',
    60: 't',
    61: 'T',
    62: 'y',
    63: 'Y',
    64: 'u',
    65: 'i',
    66: 'I',
    67: 'o',
    68: 'O',
    69: 'p',
    70: 'P',
    71: 'a',
    72: 's',
    73: 'S',
    74: 'd',
    75: 'D',
    76: 'f',
    77: 'g',
    78: 'G',
    79: 'h',
    80: 'H',
    81: 'j',
    82: 'J',
    83: 'k',
    84: 'l',
    85: 'L',
    86: 'z',
    87: 'Z',
    88: 'x',
    89: 'c',
    90: 'C',
    91: 'v',
    92: 'V',
    93: 'b',
    94: 'B',
    95: 'n',
    96: 'm'
}

def play_midi_file(obj):
    #todo more efficient playing
    last_interval = 0
    log.info("Please switch to virtualpiano window now.")
    time.sleep(3)
    log.info("Starting playback, hit Ctrl-C to exit")
    log.roll("Object is " + obj, "debug")
    for note_group in obj:
        time.sleep(note_group - last_interval)
        log.debug("Beginning playback of tick " + str(note_group))
        notes = obj[note_group]
        for i in notes.split(":")[1:]:
            log.debug("Getting ready to press " + i)
            t = Thread(target=pyautogui.press, args=(i,))
            t.start()
        last_interval = note_group
    log.success("Finished playback!")
    log.roll("Finished playback", "success")


def parse_midi_file(path):
    log.roll("Parsing a midi file: " + str(path), "info")
    output = {}
    ticks = 0
    old_ticks = 0
    invalid_notes = 0
    output_new = []
    log.info("Starting parsing of midi file. This could take a while.")
    mid = mido.MidiFile(path)
    for msg in mid:
        ticks += msg.time
        if not old_ticks == ticks:
            log.debug("Resetting outputs")
            old_ticks = ticks
            output_new = ""
        if not msg.is_meta:
            try:
                if msg.note > 96 or msg.note < 36:
                    log.warning("Skipped note with value " + str(msg.note) + " because it was out of range")
                    invalid_notes += 1
                    continue
                if msg.velocity == 0:
                    log.debug("Skipped note_on with velocity 0")
                    continue
                key_to_press = midi_defenitions[int(msg.note)]
                log.debug("Parsed note " + str(msg.note) + " as " + key_to_press)
                output_new = output_new + ":" + key_to_press
                log.debug("New output is " + str(output_new))
                output[ticks] = output_new
            except Exception as e:
                log.debug("Skipping over a message because there was no note value /e/" + str(e))
    log.success("Finished parsing track.")
    log.warning(str(invalid_notes) + " notes out of range.")
    log.debug("Object is " + str(output))
    return output
