import pigpio

class Led_Strip():
    
    def __init__(self, redgpio, greengpio, bluegpio):
        self.pi = pigpio.pi()
        
        # Default values:
        # self.REDPIN      = 21
        # self.GREENPIN    = 20
        # self.BLUEPIN     = 16
        
        self.REDPIN    = redgpio
        self.GREENPIN  = greengpio
        self.BLUEPIN   = bluegpio

        self.current_r = 0
        self.current_g = 0
        self.current_b = 0
        self.current_brightness = 0

        self.is_currently_on = False

    def TURN_ON(self, r, g, b, brightness_value):
        if (brightness_value >= 0 and brightness_value <= 100 and \
            r >= 0 and r <= 255 and \
            g >= 0 and g <= 255 and \
            b >= 0 and b <= 255):

            self.current_r          = r
            self.current_g          = g
            self.current_b          = b
            self.current_brightness = brightness_value

            self.pi.set_PWM_dutycycle(self.REDPIN    , r * (brightness_value / float(100)))
            self.pi.set_PWM_dutycycle(self.GREENPIN  , g * (brightness_value / float(100)))
            self.pi.set_PWM_dutycycle(self.BLUEPIN   , b * (brightness_value / float(100)))

            self.is_currently_on = True
        else:
            print("Value is outside the allowed range.")

    def TURN_ON_PRESET(self, preset_name, brightness_value):
        if preset_name == "AQUA":
            self.TURN_ON(64, 224, 208, brightness_value)
        elif preset_name == "BLUE":
            self.TURN_ON(190, 169, 222, brightness_value)
        elif preset_name == "BLUE_VIOLET":
            self.TURN_ON(138, 43, 226, brightness_value)
        elif preset_name == "GREEN":
            self.TURN_ON(226, 238, 130, brightness_value)
        elif preset_name == "LAVENDER":
            self.TURN_ON(255, 159, 159, brightness_value)
        elif preset_name == "SADDLE_BROWN":
            self.TURN_ON(139, 69, 19, brightness_value)
        else:
            print("There is no such preset.")

    def CHANGE_BRIGHTNESS(self, brightness_value):
        self.TURN_ON(self.current_r, self.current_g, self.current_b, brightness_value)

    def SET_RGB (self, r, g, b):
        self.TURN_ON(int(r), int(g), int(b), self.current_brightness)

    def TURN_OFF(self):
        self.pi.set_PWM_dutycycle(self.REDPIN     , 0.0)
        self.pi.set_PWM_dutycycle(self.GREENPIN   , 0.0)
        self.pi.set_PWM_dutycycle(self.BLUEPIN    , 0.0)
        self.is_currently_on = False

    def GET_POWER_STATUS(self):
        if self.is_currently_on:
            return "ON"
        return "OFF"
