#!/bin/bash
CHIP="gpiochip0"
LINE="3"

while true; do 
if gpioget -c "$CHIP" "$LINE" | grep -q inactive; then START=$(date +%s) 

while gpioget -c "$CHIP" "$LINE" | grep -q inactive; do NOW=$(date +%s)

if (( NOW - START >= 3 )); 
then systemctl poweroff;  exit 0 
fi 
sleep 0.1
done 
fi 
sleep 0.1 
done



