from sense_hat import SenseHat from time import time
from time import sleep
sense = SenseHat() sense.show_message("Hello Drake!")
temp = round(sense.get_temperature()*1.8 + 32)
humidity = round(sense.get_humidity())
pressure = round(sense.get_pressure())
message = 'Temp. : %dF Humidity : %d perc.' %(temp,humidity)
sense.show_message(message) sense.clear()
r = [255,0,0]
o = [255,127,0] y = [255,255,0] g = [0,255,0]
b = [0,0,255]
i = [75,0,130] v = [159,0,255] e = [0,0,0]
image = [ e,e,r,r,r,r,e,e, e,r,g,g,g,g,r,e, r,g,r,g,r,r,g,r, r,g,g,g,g,g,g,r, r,g,r,g,g,r,g,r, r,g,g,r,r,g,g,r, e,r,g,g,g,g,r,e, e,e,r,r,r,r,e,e ]
sense.set_pixels(image) sleep(5)
sense.clear()
image = [ b,b,b,b,b,b,b,b, b,b,b,b,b,b,b,b, b,b,b,b,b,b,b,b, b,b,b,b,b,b,b,b, b,b,b,b,b,b,b,b, b,b,b,b,b,b,b,b, b,b,b,b,b,b,b,b, b,b,b,b,b,b,b,b ]
sense.set_pixels(image)
