from flask import Flask, jsonify
import lamp_config

# init
device_names = [
    "YEELIGHT",
    "GALVEE"
]

common_actions = [
    "TOGGLE_POWER"
]

# ========== Return Codes ========== 
#  0    = Everything is fine
# -1    = No such device
# -2    = ?
# ========== Debugging ==========
@app.route('/')
def hello():
    return "Hello."

@app.route('/jsontest')
def jsontest():
    return jsonify(
        status="Success",
        code=0,
        message="Also, hello. This is the expected json output from this software.",
    )
# ========== END Debugging END ========== 
    
@app.route('/control/<device_name>/<action>')
def control(device_name, action):
    if device_name.lower() == "YEELIGHT":
        if action == "TOGGLE_POWER":
            pylight.selection(3)
        else:
            pass
            
        pass
    else if device_name.lower() == "GALVEE":
        if action == "TOGGLE_POWER":
            pass
        pass
    else:
        return return_code(-1)
        

def return_code(code):
    if code == 0:
        return jsonify(
            status="Success",
            code=0,
            message="Everything is fine."
        )
    elif code == -1:
        return jsonify(
            status="Failure",
            code=-1,
            message="No such device."
        )
    else:
        println("WARNING: There is no such error code.")

if __name__ == '__main__':
    print("Starting up (native Flask)...")
    app.run(host='0.0.0.0', threaded=True)