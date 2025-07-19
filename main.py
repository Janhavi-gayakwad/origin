import os
import eel

# Initialize the frontend folder
eel.init("www")

# OPTIONAL: Launch Edge manually (custom kiosk mode)
os.system('start msedge.exe --app="http://localhost:8000/index.html"')

# Start Eel server
eel.start('index.html', mode=None, host='localhost', block=True)
