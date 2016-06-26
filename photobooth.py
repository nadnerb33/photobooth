
from gpiozero import LED, Button
from signal import pause
import time
import os
import ftplib


print "Photo booth app running..." 



#set hardware pins
red_led = LED(4)
green_led = LED(18)
button = Button(15)

green_led.on()

def start_booth():
    green_led.off()
    id = str(int(time.time()))
    print id
    print('starting booth')
    print "Get ready..."
    #p = Popen(['./webcam.sh ', id])
    os.system("./webcam.sh "+id+" 0")
    
    #disable start button
    button.when_pressed =  time.sleep(0.1)
    
    #time.sleep(4)

    #print countdown
    print "3..."
    time.sleep(1)
    print "2..."
    time.sleep(1)
    print "1..."
    time.sleep(1)
    #p.terminate()
    print "SNAP!"
    red_led.on()
    take_photo(id)
    #p = Popen(['./webcam.sh '+id +' 1'])
    os.system("./webcam.sh "+id+" 1")
    print "processing..."
    show_photo()
    #time.sleep(3) #give time for gif to generate?
    upload_photo(id)
    #enable button
    red_led.off()
    green_led.on()
    button.when_pressed =  start_booth
    #p.terminate()
    print "Done!"
    print "Waiting for user to press button again"

def take_photo(id):
	print "taking photo"
	os.system("fswebcam -r 1280x720 -q -S 2 --no-banner " + id + "/" + id + ".jpg")

def show_photo():
	print "showing photo"

def upload_photo(id):
    print "uploading photo"
    session = ftplib.FTP('s574521753.websitehome.co.uk','u80767654-photobooth','photobooth')
    file = open(id+'/'+id+'.jpg','rb')                  # file to send
    session.storbinary('STOR '+id+'.jpg', file)     # send the file
    file = open(id+'/'+id+'.gif','rb')                  # file to send
    session.storbinary('STOR '+id+'.gif', file)     # send the file
    file.close()                                    # close file and FTP
    session.quit()
    print "upload complete"


button.when_pressed = start_booth


pause()
