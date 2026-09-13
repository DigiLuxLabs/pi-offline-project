# Raspberry Pi 4 Power Button

Hardware: 
-Momentary Push Button
-Physical pin 5: GPIO3
-Physical pin 6: Ground 

Behavior: 
-Quick press while running: no shutdown
-Hold approximately 3 seconds: clean shutdown
-When PiSugar remains powered, GPIO3 can be used for wake/start

Software: 
-Scripts/power-button.sh
-systemd/power-button.service

The systemd service automatically starts the button monitor at boot
