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
