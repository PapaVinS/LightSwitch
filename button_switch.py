import pigpio
from datetime import datetime
from time import sleep
import requests
from sensitive_information import button_pin

# Init
pi = pigpio.pi()
BUTTONPIN = button_pin

pi.set_mode(BUTTONPIN, pigpio.INPUT)
pi.set_pull_up_down(BUTTONPIN, pigpio.PUD_DOWN)

# Endpoint
URL = "http://localhost:7777/control/led_strip/toggle_power"

# Send request
while True: # Run forever
    if pi.read(button_pin) == 0:
        # print("Button was pushed!")
        # dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        # print("date and time =", dt_string)	

        # HTTP GET to toggle lamp power (it's working)
        print(requests.get(url = URL))
        sleep(0.4)