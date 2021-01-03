from yeelight import Bulb
import argparse
# from os import system
# system('cls||clear')

# not the master file!
# ini copotan, gue copas dari main repo di laptop

parser = argparse.ArgumentParser(description="Configure your Yeelight lamp.")
parser.add_argument("-m", "--manual", action='store_true', help="Enables manual configuration.")
args = parser.parse_args()

lamp = Bulb("")
effect_choice = "smooth"

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

def preset_execute(preset_choice):
    global lamp

    if (preset_choice == 1):
        lamp.turn_on
        lamp.set_rgb(245, 145, 0)
    elif (preset_choice == 2):
        lamp.turn_on
        lamp.set_color_temp(6417)
    else:
        return "There is no preset like that."
    
    return("Preset selected!")

def launch(lamp_ip):
    # init
    changeLamp(lamp_ip)
    manualMode = args.manual
       
    # yet another menu loop
    try:
        while(manualMode == True):
            print(options)
            selection(int(input("Choice: ")))
            print("")
        else:
            print("NOTICE: The default action is power toggle.")
            print("Use '-m' parameter to enter manual customization mode")
            selection(3)
    except KeyboardInterrupt:
        print("WARNING: Force closing the program.")

def selection(choice):
    global effect_choice
    
    if (choice == 1):
        print("Turning on...")
        lamp.turn_on(effect = effect_choice)
    
    elif (choice == 2):
        print("Turning off...")
        lamp.turn_off(effect = effect_choice)
    
    elif(choice == 3):
        print("Toggling...")
        lamp.toggle()
    
    elif(choice == 4):
        lamp.set_brightness(int(input("New brightness (in percent): ")))
    
    elif(choice == 5):
        r = int(input("Red value: "))
        g = int(input("Green value: "))
        b = int(input("Blue value: "))
        lamp.set_rgb(r, g, b)
            
    elif(choice == 6):
        h = int(input("Hue value: "))
        s = int(input("Saturation value: "))
        lamp.set_hsv(h, s)
            
    elif(choice == 7):
        lamp.set_color_temp(int(input("New color temp: ")))
            
    elif(choice == 8):
        print("Available presets:")
        print(presets)
        print(
            preset_execute(int(input("Preset choice: ")))
            )
        
    elif(choice == 9):
        new_ip = input("New yeelight IP: ")
        changeLamp(new_ip)
    
    elif(choice == 10):
        print(lamp.get_properties())
    
    elif(choice == 0):
        # exit here
        # raise Exception("some exception happened")
        print("Exiting...")
        exit()
    
    else:
        print("There is no command with that number.")

def changeLamp(lamp_ip):
    global lamp
    lamp = Bulb(lamp_ip)

if __name__ == "__main__":
    launch("192.168.177.11")