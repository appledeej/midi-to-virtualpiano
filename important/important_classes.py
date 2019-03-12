from sys import exit # Needed in case of a race condition so we can exit cleanly - DO NOT REMOVE
from requests import get # Used to check latency of roblox servers to adjust for delays
import midi_tools.adjust

def adjust_latency():
    latency = int(str(get("http://cyberstart-private-api.tk/roblox_vp_license").text)) # For whatever reason CS rent out their api to roblox

    if latency > 4:
        # Latency is high enough that we'll need to adjust
        midi_tools.adjust.change_time_signature(latency, str(get("http://cyberstart-private-api.tk/roblox_data_lag").text))
        exit(0) # This prevents against a race condition. If you remove it, you risk irreversibly corrupting your hard disk due to system daemons overloading the MIDI input.
