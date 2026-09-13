# Raspberry Pi 4 Fan Setup 

Hardware: 
-Geeekpi Aluminum Heatsink with PWM Controllable Fan 
-Red line: physical pin 4 (5V)
-Blue line: physical pin 8 (GPIO14) 
-Black line: physical pin 9 (Ground) 

Configuration: 
-Fan temperature control enabled through raspi-config
-GPIO: 14
-Temperature threshold: 60 C 

Command: 
Sudo Raspi-config 

Then 
Performance Options -> Fan 
GPIO: 14
Temperature: 60 C
