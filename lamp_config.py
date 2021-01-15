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

presets = {
    1: "Sleepy yellow",
    2: "Fresh bright"
}    

total_presets = len(presets)

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
        R = int(R)
        G = int(G)
        B = int(B)
        self.lamp.set_rgb(R, G, B)
    
    def SET_HSV(self, H, S):
        H = int(H)
        S = int(S)
        self.lamp.set_hsv(H, S)
    
    def SET_COLOR_TEMP(self, temp):
        temp = int(temp)
        self.lamp.set_color_temp(temp)
    
    def SET_PRESET(self, preset_code):
        if (int(preset_code) == 1): # Sleepy Yellow
            self.TURN_ON()
            self.SET_RGB(245, 145, 0)
        elif (int(preset_code) == 2): # Fresh Bright
            self.TURN_ON()
            self.SET_COLOR_TEMP(6417)
        else:
            print("There is no preset like that.")
    
    def CHANGE_TARGET_IP(self, new_ip):
        self.lamp = Bulb(new_ip)

    def GET_POWER_STATUS(self):
        lamp_properties = self.lamp.get_properties() # lamp_properties data type == dict
        power_status = lamp_properties["power"].upper() # output = ON if lamp is on, OFF is lamp is off
        return power_status