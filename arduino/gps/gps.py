# import module
from geopy.geocoders import Nominatim
import pgeocode
from serial_readgps import serial #ff

def main():

        usbport = '/dev/ttyACM0' #usb from arduino ff
        connection=serial.serial_connect(usbport, 9600,) #ff

        if (serial.inWaiting()>0):
                myData = serial.readlines()
                                                   #ff
                lat=str(myData[len(myData)-3])
                lon=(myData[len(myData)-2])

        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.reverse(lat+","+lon)
        
        #traverse the data
        #city = address.get('city', '')
        #state = address.get('state', '')
        #country = address.get('country', '')
        #code = address.get('country_code')
        zipcode = location.raw['address'].get('postcode')
        #print('City : ', city)
        #print('State : ', state)
        #print('Country : ', country)
        #print('Zip Code : ', zipcode)

        nomi = pgeocode.Nominatim('in')
        res = nomi.query_postal_code(zipcode)
        res_main=res.place_name+" "+res.state_name
        return res_main


if __name__=="__main__":
        # Latitude & Longitude input
        Latitude = "10.9034846"
        Longitude = "76.9791687"
        print(main(Latitude,Longitude))
