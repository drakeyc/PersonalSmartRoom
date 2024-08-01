import sys
import time
import subprocess
import uuid
import requests
import pprint
import csv
from wia import Wia
from numpy import linalg as np 
from picamera import PiCamera 
from picamera import PiResolution 
from sense_hat import SenseHat 
import webbrowser

#Method that runs the main menu,
#allows a user to create a new user or attempt to sign in. 

def mainMenu():

  print("1: Create User") 
  print("2: Verify User") 
  print("0: Exit")
  selection=input("Enter Choice: ")
  
 if selection == "1": 
   createUser() 
   mainMenu()
elif selection == "2": 
  verifyUser() 
  mainMenu()
elif selection == "0": 
  exit()
else:
  print("Invalid choice") 
  mainMenu()


#Uses the Pi camera module to take a picture, trigger an event from Wia #which uses AWS face detection to determine if there is a face, using JS,
#the relevant face landmark data is extracted and added to the "user" database. 


#def createUser():
def createUser():
camera = PiCamera()
camera.resolution = (1000,800)
camera.start_preview()
time.sleep(2)
fileName = str(uuid.uuid4())+".jpeg" camera.capture('/home/pi/Desktop/'+fileName) camera.stop_preview()
camera.close()
wia = Wia()
wia.access_token = "d_sk_Dku9mWR5BvmqGBu4DlVbleEZ"
try:
wia.Event.publish(name = "user",file = '/home/pi/Desktop/'+fileName) print("")
print("Image uploading...")
time.sleep(1)
print("")
print("Image uploaded!")
print("")
except Exception as error: print(error)
#Follows the same principle of createUser() but the image data gets sent to #the "images" database. The method ecuDst() is then called, which takes in the #values from the retrieveUser() and retrieveImage() functions.
def verifyUser():

 camera = PiCamera()
camera.resolution = (1000,800)
camera.start_preview()
time.sleep(2)
fileName = str(uuid.uuid4())+".jpeg" camera.capture('/home/pi/Desktop/'+fileName) camera.stop_preview()
camera.close()
wia = Wia()
wia.access_token = "d_sk_Dku9mWR5BvmqGBu4DlVbleEZ"
try:
wia.Event.publish(name = "image",file = '/home/pi/Desktop/'+fileName) print("")
print("Image uploading...")
time.sleep(1)
print("")
print("Image uploaded!")
print("Welcome, Drake!")
print("")
sense = SenseHat()
sense.show_message("Hello Drake! A cool blue lighting and Travis Scott Radio at your service.")
temp = round(sense.get_temperature()*1.8 + 32 )
humidity = round(sense.get_humidity())
pressure = round(sense.get_pressure())
message = 'Temp. : %dF Humidity : %d perc.' %(temp,humidity)
sense.show_message(message) sense.clear()
r = [255,0,0]
o = [255,127,0] y = [255,255,0] g = [0,255,0]
b = [0,0,255]
i = [75,0,130] v = [159,0,255] e = [0,0,0]
image = [ e,e,r,r,r,r,e,e, e,r,g,g,g,g,r,e,

 r,g,r,g,r,r,g,r, r,g,g,g,g,g,g,r, r,g,r,g,g,r,g,r, r,g,g,r,r,g,g,r, e,r,g,g,g,g,r,e, e,e,r,r,r,r,e,e
]
sense.set_pixels(image) time.sleep(5) sense.clear()
image = [ b,b,b,b,b,b,b,b, b,b,b,b,b,b,b,b, b,b,b,b,b,b,b,b, b,b,b,b,b,b,b,b, b,b,b,b,b,b,b,b, b,b,b,b,b,b,b,b, b,b,b,b,b,b,b,b, b,b,b,b,b,b,b,b ]
sense.set_pixels(image) webbrowser.open('https://www.pandora.com/station/play/4226635084818175147');
print("Travis Scott Radio");
print("Welcome, Drake!")
print("Pandora station Travis Scott Radio is now playing!") print("The room temperature is" + temp + " degrees F!") print("A selection of Pandora is now playing.")
print("")
except Exception as error:
print(error)
eucDst(retrieveUser(), retrieveImage())
#clearUsers()
#Gets the landmark data back from mLab and extracts it into an array of floats
def retrieveUser():
usersMlab='https://api.mlab.com/api/1/databases/iot_db/collections/users?apiKey=795sadqyQbF6y5rMAuZivWlmcO9d1_nR' response=requests.get(usersMlab)
data=response.json()
emptyStr = ""

 user = []
for i in data:
emptyStr = emptyStr + str(i)
words = emptyStr.split(",") x=0
while x < len(words): try:
user.append(float(words[x])) except:
print("") x+=1
del user[18:] print(user)
return user
#Gets the landmark data back from mLab and extracts it into an array of floats
def retrieveImage():
imagesMlab='https://api.mlab.com/api/1/databases/iot_db/collections/images?apiKey=795sadqyQbF6y5rMAuZivWlmcO9d1 _nR'
response=requests.get(imagesMlab) data=response.json()
emptyStr = ""
image = []
for i in data:
emptyStr = emptyStr + str(i)
words = emptyStr.split(",") x=0
while x < len(words): try:
image.append(float(words[x])) except:
print("") x+=1

 del image[18:] print(image)
return image
#Takes in the user and image arrays from both the
#retrieveUser() and retrieveImage() methods. Finds the euclidean distance #of both the arrays, and subtracts them. If the result "dist" is less than #0.2 and greater than -0.2, then the programm determines that this is #correct user, and that they may enter.
def eucDst(user, image):
a = user
b = image
dist = np.norm(a) - np.norm(b) print(dist)
if dist < 0.3 and dist > -0.3:
imagesMlab='https://api.mlab.com/api/1/databases/iot_db/collections/images?apiKey=795sadqyQbF6y5rMAuZivWlmcO9d1 _nR'
response=requests.get(imagesMlab) data=response.json()
emptyStr = ""
image = []
for i in data:
emptyStr = emptyStr + str(i)
words = emptyStr.split(",") x=0
while x < len(words): try:
image.append(float(words[x])) except:
print("") x+=1
del image[18:] print(image)
return image

else: print("")
print("Unknown User") print("")
#def clearUsers():
#usersMlab='https://api.mlab.com/api/1/databases/iot_db/collections/images?apiKey=795sadqyQbF6y5rMAuZivWlmcO9d1_ nR'
#response=requests.put(usersMlab, []) #data=response.json()
#print(data)
def exit(): print("")
print("shutting down...") print("")
time.sleep(2) print("Goodbye!") print("")
time.sleep(1) sys.exit
mainMenu()
