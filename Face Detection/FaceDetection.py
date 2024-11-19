import cv2

haar_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cam= cv2.VideoCapture(0)

while True:   #infinite loop
    _, img=cam.read() #reading frames
    grayImg=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converting to grayscale

    faces = haar_cascade.detectMultiScale(grayImg, 1.3, 4)

    for(x,y,w,h) in faces: 
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),4)
    
    cv2.imshow("FaceDetection", img)

    key = cv2.waitKey(10)
    print(key)
    if key == 27: #Escape key to exit
        break

    #Checking if the window close button was clicked
    #if cv2.getWindowProperty('cameraFeed', cv2.WND_PROP_AUTOSIZE) < 0:
    #    break

cam.release()
cv2.destroyAllWindows()
