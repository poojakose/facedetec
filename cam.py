#from picamera.array import PiRGBArray
#from picamera import PiCamera
import cv2 
import time

face_cascade = cv2.CascadeClassifier('/home/pooja_kose/Downloads/pan-tilt-tracking/pan_tilt_tracking/haarcascade_frontalface_default.xml') 

cap = cv2.VideoCapture(0)

while 1:

	# read frames from a camera 
	ret, flip1 = cap.read()
        img = cv2.flip(flip1, 1) 
        pan = 100
        tilt = 100
	# convert to gray scale of each frames 
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

	# Detects faces of different sizes in the input image
	faces = face_cascade.detectMultiScale(gray, 1.3, 5) 

	for (x,y,w,h) in faces: 
		# To draw a rectangle in a face 
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]

        if (w < 150):
            print ("FAR  .... w = %d " % w)

        elif (h > 150):
            print ("NEAR   .... h = %d " % h)

        
        
        #print faces
        time.sleep(0.1)
	cv2.imshow('img',img) 

	# Wait for Esc key to stop 
	k = cv2.waitKey(30) & 0xff
	if k == 27: 
		break

# Close the window 
cap.release() 

# De-allocate any associated memory usage 
cv2.destroyAllWindows() 

