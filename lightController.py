from hue import Hue;
h = Hue(); # Initialize the class
h.station_ip = "192.168.2.169"  # Your base station IP
h.get_state(); # Authenticate, bootstrap your lighting system

l = h.lights.get('l5') # get bulb #5
#l.bri(0) # Dimmest
l.bri(255) # Brightest
#l.rgb(120, 120, 0) # [0-255 rgb values]
#l.rgb("#9af703") # Hex string
l.on()
#l.off()
#l.toggle()
#l.alert() # short alert
#l.alert("lselect") # long alert
#l.setState({"bri": 220, "alert": "select"}) # Complex send




def handleUserMessage(command):
    #TODO parse the user string.
    command.split(" ")
    print command
    #TODO get the set of nodes to work on from the device
    setOfLightsToOperateOn = ['l5']
    #TODO which function should I apply?
    funcToApply = ExtendedColorLight
    for light in setOfLightsToOperateOn:
        pass

#TODO can we use a library for colours to use strings instead of hex? 
# is there a library for that?

handleUserMessage("all brightness 255")

