from yeelight import Bulb

options = {
    1: "Turn on",
    2: "Turn off",
    3: "Toggle power",
    4: "Set brightness",
    5: "Set RGB value",
    6: "Set HSV value",
    7: "Set color temperature",
    8: "Select preset",
    9: "Change lamp",
    10: "Get lamp properties",
    0: "Exit",
}

presets = {
    1: "Sleepy yellow",
    2: "Fresh bright"
}

class Lamp():
    lamp = Bulb("")
    effect_choice = "smooth"
    
    def TURN_ON(self):
        self.lamp.turn_on(effect = self.effect_choice)
        
    def TURN_OFF(self):
        self.lamp.turn_off(effect = self.effect_choice)
        
    def TOGGLE_POWER(self):
        self.lamp.toggle()