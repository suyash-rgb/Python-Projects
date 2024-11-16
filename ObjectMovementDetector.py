import cv2
import time
import imutils

# Attempt to initialize the camera
cam = cv2.VideoCapture(0)  # Try with 0, -1, or another index if 1 does not work
time.sleep(1)

if not cam.isOpened():
    print("Error: Could not open camera.")
    exit()

firstFrame = None
area = 500

while True:
    ret, img = cam.read()
    if not ret:
        print("Error: Failed to capture image.")
        break

    text = "Normal"

    img = imutils.resize(img, width=800)
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gaussianImg = cv2.GaussianBlur(grayImg, (21, 21), 0)

    if firstFrame is None:
        firstFrame = gaussianImg
        continue

    imgDiff = cv2.absdiff(firstFrame, gaussianImg)
    threshImg = cv2.threshold(imgDiff, 25, 255, cv2.THRESH_BINARY)[1]

    threshImg = cv2.dilate(threshImg, None, iterations=2)

    cnts = cv2.findContours(threshImg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cnts = imutils.grab_contours(cnts)
    for c in cnts:
        if cv2.contourArea(c) < area:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Moving Object Detected"
    print(text)
    cv2.putText(img, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.imshow("cameraFeed", img)

    key = cv2.waitKey(10) & 0xFF  
    if key == ord("q"):
        break

    # Check if the window close button was clicked
    if cv2.getWindowProperty('cameraFeed', cv2.WND_PROP_AUTOSIZE) < 0:
        break

cam.release()
cv2.destroyAllWindows()
