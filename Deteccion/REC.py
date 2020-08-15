# This script will detect faces via your webcam.
# Tested with OpenCV3

import cv2

cap = cv2.VideoCapture(0)
# Create the haar cascade
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
fullbodyCascade = cv2.CascadeClassifier("haarcascade_fullbody.xml")
upperbodyCascade = cv2.CascadeClassifier("haarcascade_upperbody.xml")

stime=0
NotDe=0

while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()
	frame = cv2.resize(frame, (480, 320))  

	# Our operations on the frame come here
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Detect faces in the image
	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.25,
		minNeighbors=4,
		minSize=(30, 30)
		#flags = cv2.CV_HAAR_SCALE_IMAGE
	)

	fullbodies = fullbodyCascade.detectMultiScale(
		gray,
		scaleFactor=1.25,
		minNeighbors=4,
		minSize=(30, 30)
		#flags = cv2.CV_HAAR_SCALE_IMAGE
	)

	upperbodies = upperbodyCascade.detectMultiScale(
		gray,
		scaleFactor=1.25,
		minNeighbors=4,
		minSize=(30, 30)
		#flags = cv2.CV_HAAR_SCALE_IMAGE
	)

	#print("Found {0} faces!".format(len(faces)))

	# Draw a rectangle around the faces
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

	# Draw a rectangle around the fullbody
	for (x, y, w, h) in fullbodies:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

	# Draw a rectangle around the upperbody
	for (x, y, w, h) in upperbodies:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

	cont1=len(faces)
	cont2=len(fullbodies)
	cont3=len(upperbodies)



	
	if cont1>0 or cont2>0 or cont3>0 :
		stime+=1
		if stime>4:
			f= open("Movimiento.txt","w+")
			f.write("1")
			f.close() 
			#print("Movimiento detectado")
			stime=0			
				
			
	else:
		NotDe+=1
		if NotDe > 80:
			f= open("Movimiento.txt","w+")
			f.write("0")
			f.close() 
			NotDe=0

	# Display the resulting frame
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()