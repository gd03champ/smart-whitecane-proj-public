import os
import socket
import playsound
from translate_tts import transnsay

def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False

def out(des):
    if is_connected():
        print(des)
        transnsay(des,'ta')
    else:
        os.system(f'''espeak "{des}" ''')
        print(des)

out("Starting The System")

try:

    from assistant import provoke
    from push import inter
    import multiprocessing
    import time
    import gps

except:
    os("error importing")

out("system started succesfully")


if __name__ == "__main__":

    try:

        while True:

            p = multiprocessing.Process(target = inter, name = "Inter")
            p.start()

            time.sleep(4)
            p.join(4)

            if p.is_alive():
                p.terminate()

            f=open('itf.txt','r+')

            interaction = f.read()
            f.write("0")

            f.close()
            print(interaction)

            if interaction == "0":
                pass
            elif interaction == "1":
                print("👉 GPS Action")
                location="Your current location is "+gps.locate()
                out(location)

            elif interaction == "2":
                print("👉 Object Detection")
                out("Analysing environment")
                os.system("python3 obstacle.py")

            elif interaction == "3":
                print("👉 Google Assistant")
                playsound.playsound('assets/listening.mp3', True)
                provoke.okgoogle()

            elif interaction == "4":
                print("👉 Sending voice mail and live location")
                out("Sending voice mail and live location to registered mobile number")
                try:
                    os.system("python3 call.py")
                    out("Sent successfully")
                except:
                    out("Currently facing issues with server!. Try back later") 

            else:
                pass

    except KeyboardInterrupt:
        print("Main loop terminated: Ctrl C pressed 🙂")
        exit()



