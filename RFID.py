import RPi.GPIO as GPIO
from wia import Wia
from mfrc522 import SimpleMFRC522
wia = Wia()
wia.access_token = "d_sk_WCl5qzwRr9VkXJ5z5wnt33hZ" reader = SimpleMFRC522()
try:
  id, text = reader.read()
  print(id) 
  wia.Event.publish(name="RFiD",data=text)
finally: 
  GPIO.cleanup()
