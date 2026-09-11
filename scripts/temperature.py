from pathlib import Path
from time import sleep 

TEMP_FILE = Path("/sys/class/thermal/thermal_zone0/temp")
FAN_THRESHOLD = 55.0

while True: 
    celsius = int(TEMP_FILE.read_text()) / 1000
    fahrenheit = (celsius * 9 / 5) + 32

    print (f"CPU temperature:{fahrenheit:.1f} F")
    if celsius >= FAN_THRESHOLD:
        print ("Fan threshold reached")

sleep(5)
