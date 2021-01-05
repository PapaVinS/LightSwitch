from yeelight import Bulb

# options = {
#     1: "Turn on",
#     2: "Turn off",
#     3: "Toggle power",
#     4: "Set brightness",
#     5: "Set RGB value",
#     6: "Set HSV value",
#     7: "Set color temperature",
#     8: "Select preset",
#     9: "Change lamp",
#     10: "Get lamp properties",
#     0: "Exit",
# }

# presets = {
#     1: "Sleepy yellow",
#     2: "Fresh bright"
# }    

class Lamp():
    
    def __init__(self, host_ip):
        self.lamp = Bulb(host_ip)
        self.effect_choice = "smooth"
    
    def TURN_ON(self):
        self.lamp.turn_on(effect = self.effect_choice)
        
    def TURN_OFF(self):
        self.lamp.turn_off(effect = self.effect_choice)
        
    def TOGGLE_POWER(self):
        self.lamp.toggle()
        
    def SET_BRIGHTNESS(self, brightness_value):
        brightness_value = int(brightness_value)
        if (brightness_value) >= 0 and (brightness_value) <= 100:
            self.lamp.set_brightness(brightness_value)
        else:
            print("Value is outside the allowed range.")
    
    def SET_RGB(self, R, G, B):
        pass
    
    def SET_HSV(self, H, S):
        pass
    
    def SET_COLOR_TEMP(self, temp):
        pass
    
    def SET_PRESET(self, preset_code):
        if (int(preset_code) == 1):
            lamp.turn_on
            lamp.set_rgb(245, 145, 0)
        elif (int(preset_code) == 2):
            lamp.turn_on
            lamp.set_color_temp(6417)
        else:
            print("There is no preset like that.")
        return("Preset selected!")
    
    def CHANGE_TARGET_IP(self, new_ip):
        pass
    
    
    