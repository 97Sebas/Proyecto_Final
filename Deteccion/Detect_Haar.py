# This script will detect faces via your webcam.
# Tested with OpenCV3

import cv2

cap = cv2.VideoCapture(0)

# Create the haar cascade

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cantidad=0
while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()

	# Our operations on the frame come here
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Detect faces in the image
	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30)
		#flags = cv2.CV_HAAR_SCALE_IMAGE
	)

	#print("Se encontró {0} personas en el lugar!".format(len(faces)))
	
	if len(faces) > 0:
		cantidad+=len(faces)
		#print("Se encontró {0} movimientos en el lugar!".format(len(faces)))
		if cantidad > 5:
			print("Hay movimiento humano")
			f= open("guru99.txt","w+")
			f.write("\nCantidad de detecciones en zona alta : %d\r\n" % (cantidad))
			cantidad=0
		with open('out.txt', 'a') as f:
    		for i in range(0,2):
        		x[i] = np.array([1,2,3,8,3])
        		np.savetxt(f, x[i])

	# Draw a rectangle around the faces
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


	# Display the resulting frame
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()