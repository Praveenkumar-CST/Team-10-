import cv2

drone_cascade = cv2.CascadeClassifier('myharr.xml')
cap = cv2.VideoCapture(0)
def detect() :

    print("!!!!!ALERTT!!!!")
    print("DRONE FOUNDED")

def dr1():
    drone1 = drone_cascade.detectMultiScale(gray, 5.5, 4)
    for (x, y, w, h) in drone:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0,255), 2)

    cv2.imshow('drone1', img)
while True:

    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    drone = drone_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in drone:


     cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    d = img.all()
    if d== False:
        cv2.putText(img, "    !!!!ALERT!!!! DRONE DETECTED", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)
    else:
        cv2.putText(img, "         DRONE NOT DETECTED  ", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 1)




    cv2.imshow('drone', img)
    dr1()




    if d == False:
           detect()

    else:
        print("NOT DETECT")

    if d == False:
    #sound()
     _, img = cap.read()
    try:
       k = cv2.waitKey(30) & 0xff
    except KeyboardInterrupt:
        pass
    if k==27:

        break

cap.release()