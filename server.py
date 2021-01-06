from flask import Flask, jsonify, request
from lamp_config import Lamp
from led_strip_config import Led_Strip

# ========== init ========== 
lamp        = Lamp("192.168.177.11")
led_strip   = Led_Strip(21, 20, 16)

backend = Flask(__name__)
# ========== END init END ==========

# ========== Return Codes ========== 
#  0    = Everything is fine
# -1    = No such device
# -2    = No such action
# -3    = Missing arguments
# -4    = ?
# ========== Debugging ==========
@backend.route('/')
def hello():
    return "Hello."

@backend.route('/jsontest')
def jsontest():
    return jsonify(
        status="Success",
        code=0,
        message="Also, hello. This is the expected json output from this software.",
    )
# ========== END Debugging END ========== 

@backend.route('/control/<device_name>/<action>')
@backend.route('/control/<device_name>', defaults={'action' : "NO_DEVICE"})
@backend.route('/control/', defaults={'device_name' : "NO_DEVICE", 'action' : "NO_DEVICE"})
def control(device_name, action):
    device_name = device_name.upper()
    action = action.upper()
    uppercase_request_args = uppercase_dict(request.args)
    
    if device_name == "YEELIGHT":
        if action == "TURN_ON":
            lamp.TURN_ON()
            return return_code(0, "Turning on...")
        
        elif action == "TURN_OFF":
            lamp.TURN_OFF()
            return return_code(0, "Turning off...")
        
        elif action == "TOGGLE_POWER":
            lamp.TOGGLE_POWER()
            return return_code(0, "Toggling power...")
        
        elif action == "SET_BRIGHTNESS":
            # raw_brightness = request.args.get("brightness_value")
            raw_brightness = uppercase_request_args.get("BRIGHTNESS_VALUE")

            if type(raw_brightness) is not type(None):
                brightness_value = int(raw_brightness)
            else:
                return return_code(-3, "No brightness value is inserted.")

            #brightness_value = all_get_request_args.get("brightness_value")
            if type(brightness_value) is not type(None) and \
                (brightness_value) >= 0 and (brightness_value) <= 100:

                lamp.SET_BRIGHTNESS(brightness_value)
                return return_code(0, "Setting brightness...")
            else:
                return return_code(-3, "Make sure brightness value is between 0 and 100.")
        
        elif action == "SET_RGB":
            pass
        
        elif action == "SET_HSV":
            pass
        
        elif action == "SET_COLOR_TEMP":
            pass
        
        elif action == "SET_PRESET":
            pass
        
        elif action == "CHANGE_TARGET_IP":
            pass
        
        else:
            return return_code(-2)
    
    
    
    
    
            
        pass
    elif device_name == "LED_STRIP":
        if action == "TURN_ON":
            led_strip.TURN_ON(255, 255, 255, 100)
            return return_code(0)

        elif action == "TOGGLE_POWER":
            if led_strip.is_currently_on:
                led_strip.TURN_OFF()
                return return_code(0, "Turning off...")
            else:
                led_strip.TURN_ON_PRESET("LAVENDER", 20)
                return return_code(0, "Turning on...")

        elif action == "SET_RGB":
            led_strip.SET_RGB()

        elif action == "TURN_OFF":
            led_strip.TURN_OFF()
            return return_code(0, "Turning off...")

        else:
            return return_code(-2)
    else:
        #return(device_name)
        return return_code(-1)
        

def uppercase_dict(old_dict):
    new_uppercase_dict = {}
    for key in old_dict:
        new_uppercase_dict[key.upper()] = old_dict[key]
    return new_uppercase_dict

def return_code(code, ext_message = ""):
    if code == 0:
        return jsonify(
            status="Success",
            code=code,
            code_details="Everything is fine.",
            message=ext_message
        )
    elif code == -1:
        return jsonify(
            status="Failure",
            code=code,
            code_details="No such device.",
            message=ext_message
        )
    elif code == -2:
        return jsonify(
            status="Failure",
            code=code,
            code_details="No such action.",
            message=ext_message
        )
    elif code == -3:
        return jsonify(
            status="Failure",
            code=code,
            code_details="Missing or wrong argument(s).",
            message=ext_message
        )
    else:
        println("WARNING: There is no such error code.")

if __name__ == '__main__':
    print("Starting up (native Flask)...")
    backend.run(host='0.0.0.0', threaded=True)
