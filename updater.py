import mysql.connector
from serial_readgps import serial
from datetime import datetime
import time


def main():
  #connecting to mysql database

  mydb = mysql.connector.connect(
    host="sql6.freesqldatabase.com",
    port="3306",
    user="sql6514013",
    password="Z64ed66aI7",
    database="sql6514013"
  )
  mycursor = mydb.cursor()


  #retriving location data from serial

  usbport = '/dev/ttyACM0'
  connection=serial.serial_connect(usbport, 9600,)
  if (serial.inWaiting()>0):

    myData = serial.readlines()
    lat=str(myData[len(myData)-3])
    lon=str(myData[len(myData)-2])


  #retriving data and time
  now = datetime.now()

  date = now.strftime("%d")
  month = now.strftime("%m")
  year = now.strftime("%Y")

  hours = now.strftime("%H")
  minutes = now.strftime("%M")
  seconds = now.strftime("%S")


  #defining command for data update into dtaabase
  cmd = f"INSERT INTO data VALUES ({lat}, {lon}, '{year}-{month}-{date}', '{hours}:{minutes}:{seconds}')"
  show = "select * from data"

  mycursor.execute(cmd)
  mydb.commit()

  print(f"Location data updated")

  #printout updated list to console
  mycursor.execute(show)
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)

  mydb.close()
  mycursor.close()

while True:
  main()
  time.sleep(1800)