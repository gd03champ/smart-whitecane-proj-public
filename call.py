# Find the Sinch phone number assigned to your app
# and your application key and secret 
# at dashboard.sinch.com/voice/apps
import requests
import gps
import os
from serial_readgps import serial  #ff
import g_authenticate  #ff



key = ""
secret = ""
fromNumber = ""
to = ""
locale = "en-US"
url = "https://calling.api.sinch.com/calling/v1/callouts"
name = g_authenticate.get_name()

#custom variables
location = gps.locate()

payload = {
  "method": "ttsCallout",
  "ttsCallout": {
    "cli": fromNumber,
    "destination": {
      "type": "number",
      "endpoint": to
    },
    "locale": locale,
    "text": f"{name} is in the location {location}. and might need your help!. More information will be sent in a message"
  }
}

headers = { "Content-Type": "application/json" }

response = requests.post(url, json=payload, headers=headers, auth=(key, secret))

data = response.json()
print(data)

#sending message

name = g_authenticate.get_name()
location = gps.locate()

usbport = '/dev/ttyACM0'
connection=serial.serial_connect(usbport, 9600,)
if (serial.inWaiting()>0):
  myData = serial.readlines()
  lat=str(myData[len(myData)-3])
  lon=str(myData[len(myData)-2])

  map_link = f"https://www.google.com/maps/search/?api=1&query={lat}%2C{lon}"
  content = f"{name} is in the location of {location} and might need your help!. Google map ink {map_link}"

  cmd = '''curl -X POST -H "Authorization: Bearer cbedd4e12e034f279447c4GD17afe28f" -H "Content-Type: application/json" -d '{ "from": "447520651700", "to": [ "918825648984" ], "body": " '''+ content + '''" }' "https://sms.api.sinch.com/xms/v1/f85ebdfc9c5048a18GD4196276e60827/batches" '''

  os.system(cmd)
