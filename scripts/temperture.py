from pathlib import Path
from time import sleep 

TEMP_FILE = Path("/sys/class/thermal/thermal_zone0/temp")
FAN_THRESHOLD = 55.0

while True: 
	temperature =
int(TEMP_FILEl.read.text())/1000

	print (f"CPU temperature:
{temperature:.1f} C")
	if temperature >=FAN_THRESHOLD:
	print ("Fan threshold reached")

sleep(5)
