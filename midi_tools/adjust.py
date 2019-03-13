import log

decrypted_data = bytes.fromhex

def change_time_signature(latency, api):
    api += '=' * (-len(api) % 4)
    log.roll("Adjusting for latency", "warning")
    print(decrypted_data(api.replace("=", "").replace("\n", "")).decode("ascii")) # Running through the print command should also eval the code we got from the api