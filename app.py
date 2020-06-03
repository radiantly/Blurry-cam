import cv2
import pyfakewebcam

# Capture device
cap = cv2.VideoCapture('/dev/video0')

height, width = 480, 640

newHeight, newWidth = height // 5, width // 5

cap.set(cv2.CAP_PROP_FRAME_WIDTH , width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cap.set(cv2.CAP_PROP_FPS, 30)

# Initialize webcam
fake = pyfakewebcam.FakeWebcam('/dev/video20', width, height)

while cap.isOpened():

    _, frame = cap.read()
    

    # To convert to grayscale
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Pixelize image by resizing to newWidth and newHeight
    temp = cv2.resize(frame, (newWidth, newHeight), interpolation=cv2.INTER_LINEAR)
    frame = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)

    # Blur image - increase the numbers below to increase the blur
    frame = cv2.blur(frame, (15, 15))

    # Send frame to fake webcam
    rgbframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    fake.schedule_frame(rgbframe)

    # Uncomment this to see a preview window
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

else:
    print("Unable to open capture device.")

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()