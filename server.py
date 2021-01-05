from flask import Flask, jsonify, request
from lamp_config import Lamp
from led_strip_config import Led_Strip

# ========== init ========== 
lamp        = Lamp("192.168.177.11")
led_strip   = Led_Strip(21, 10, 16)

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
def control(device_name, action):
    device_name = device_name.upper()
    action = action.upper()
    
    if device_name == "YEELIGHT":
        if action == "TURN_ON":
            lamp.TURN_ON()
            return return_code(0)
        
        elif action == "TURN_OFF":
            lamp.TURN_OFF()
            return return_code(0)
        
        elif action == "TOGGLE_POWER":
            lamp.TOGGLE_POWER()
            return return_code(0)
        
        elif action == "SET_BRIGHTNESS":
            brightness_value = request.args.get("brightness_value")
            if type(brightness_value) is not type(None):
                lamp.SET_BRIGHTNESS(brightness_value)
                return return_code(0)
            else:
                return return_code(-3)
        
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
        if action == "TOGGLE_POWER":
            if led_strip.is_currently_on:
                led_strip.TURN_OFF()
                return return_code(0)
            else:
                led_strip.TURN_ON_PRESET("LAVENDER", 20)
                return return_code(0)
        else:
            return return_code(-2)
    else:
        return return_code(-1)
        

def return_code(code):
    if code == 0:
        return jsonify(
            status="Success",
            code=code,
            message="Everything is fine."
        )
    elif code == -1:
        return jsonify(
            status="Failure",
            code=code,
            message="No such device."
        )
    elif code == -2:
        return jsonify(
            status="Failure",
            code=code,
            message="No such action."
        )
    elif code == -3:
        return jsonify(
            status="Failure",
            code=code,
            message="Missing arguments."
        )
    else:
        println("WARNING: There is no such error code.")

if __name__ == '__main__':
    print("Starting up (native Flask)...")
    backend.run(host='0.0.0.0', threaded=True)
