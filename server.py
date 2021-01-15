from flask import Flask, jsonify, request
from lamp_config import Lamp, total_presets
from led_strip_config import Led_Strip
from temperature_config import read_temperature

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
# -4    = Incorrect argument range
# -5    = ?
# ========== END Return Codes END ==========

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

@backend.route('/read_temperature')
def temperature():
    return return_code(0, read_temperature())

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
            brightness_value = uppercase_request_args.get("BRIGHTNESS_VALUE")

            if isNotEmpty(brightness_value):
                if brightness_isCorrectRange(brightness_value):
                    lamp.SET_BRIGHTNESS(brightness_value)
                    return return_code(0, "Setting brightness...")
                return return_code(-4, 100)
            return return_code(-3)
        
        elif action == "SET_RGB":
            r_value = uppercase_request_args.get("R_VALUE")
            g_value = uppercase_request_args.get("G_VALUE")
            b_value = uppercase_request_args.get("B_VALUE")

            if isNotEmpty(r_value) and isNotEmpty(g_value) and isNotEmpty(b_value):
                if RGB_isCorrectRange(r_value) and RGB_isCorrectRange(g_value) and RGB_isCorrectRange(b_value):
                    lamp.SET_RGB(r_value, g_value, b_value)
                    return return_code(0, "Changing RGB value...")
                return return_code(-4, 255)
            return return_code(-3)
        
        elif action == "SET_HSV":
            h_value = uppercase_request_args.get("H_VALUE")
            s_value = uppercase_request_args.get("S_VALUE")

            if isNotEmpty(h_value) and isNotEmpty(s_value):
                if RGB_isCorrectRange(h_value) and RGB_isCorrectRange(s_value):
                    lamp.SET_HSV(h_value, s_value)
                    return return_code(0, "Changing HSV...")
                return return_code(-4, 255)
            return return_code(-3)
        
        elif action == "SET_COLOR_TEMP":
            temperature_value = uppercase_request_args.get("TEMP_VALUE")
            
            if isNotEmpty(temperature_value):
                if temperature_isCorrectRange(temperature_value):
                    lamp.SET_COLOR_TEMP(temperature_value)
                    return return_code(0, "Setting temperature value...")
                return return_code(-4.1)
            return return_code(-3)
        
        elif action == "SET_PRESET":
            preset_value = uppercase_request_args.get("PRESET_VALUE")
            
            if isNotEmpty(preset_value):
                if preset_isCorrectRange(preset_value):
                    lamp.SET_PRESET(preset_value)
                    return return_code(0, "Setting preset...")
                return return_code(-4, total_presets)
            return return_code(-3)
        
        elif action == "CHANGE_TARGET_IP":
            target_ip = uppercase_request_args.get("TARGET_IP")

            if isNotEmpty(target_ip):
                lamp.CHANGE_TARGET_IP(target_ip)
                return return_code(0, "Lamp change successful.")
            return return_code(-3, "Incorrect arguments.")

        else:
            return return_code(-2)
    
    elif device_name == "LED_STRIP":
        if action == "TURN_ON":
            led_strip.TURN_ON(255, 255, 255, 100)
            return return_code(0)

        elif action == "TOGGLE_POWER":
            if led_strip.is_currently_on:
                led_strip.TURN_OFF()
                return return_code(0, "Turning off...")
            else:
                led_strip.TURN_ON_PRESET("BLUE_VIOLET", 20)
                return return_code(0, "Turning on...")

        elif action == "SET_RGB":
            r_value = uppercase_request_args.get("R_VALUE")
            g_value = uppercase_request_args.get("G_VALUE")
            b_value = uppercase_request_args.get("B_VALUE")

            if isNotEmpty(r_value) and isNotEmpty(g_value) and isNotEmpty(b_value):
                led_strip.SET_RGB(r_value, g_value, b_value)
                return return_code(0, "Changing RGB value...")
            return return_code(-3)

        elif action == "TURN_OFF":
            led_strip.TURN_OFF()
            return return_code(0, "Turning off...")

        else:
            return return_code(-2)
    else:
        return return_code(-1)
        
# ========== utils ==========

# Essential to make GET arguments case insensitive
def uppercase_dict(old_dict):
    new_uppercase_dict = {}
    for key in old_dict:
        new_uppercase_dict[key.upper()] = old_dict[key]
    return new_uppercase_dict

# Make sure arguments are not empty
def isNotEmpty(argument):
    return type(argument) is not type(None)

# Make sure RGB value is within range
def RGB_isCorrectRange(single_color_value):
    return int(single_color_value) >= 0 and int(single_color_value) <= 255

# Make sure brightness value is within range
def brightness_isCorrectRange(brightness_value):
    return int(brightness_value) >= 0 and int(brightness_value) <= 100

# Make sure temperature value is within range
def temperature_isCorrectRange(temperature_value):
    return int(temperature_value) >= 1700 and int(temperature_value) <= 6500

#Make sure presets is available
def preset_isCorrectRange(preset_value):
    return int(preset_value) >= 1 and int(preset_value) <= total_presets

# Return code builder
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
            code_details="Missing or incorrect argument(s).",
            message=ext_message
        )
    elif code == -4:
        return jsonify(
            status="Failure",
            code=code,
            code_details="Incorrect argument(s) range.",
            message="Make sure the value is between 0-%s" %ext_message
        )
    elif code == -4.1:
        return jsonify(
            status="Failure",
            code=code,
            code_details="Incorrect argument(s) range.",
            message="Make sure the temperature value is between 1700-6500"
        )
    else:
        print("WARNING: There is no such error code.")

# ========== END utils END ==========

if __name__ == '__main__':
    print("Starting up (native Flask)...")
    backend.run(host='0.0.0.0', threaded=True)
