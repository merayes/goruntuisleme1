import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

while True:
    ret,goruntu = kamera.read()

    reda = np.array([0,100,100])
    redb = np.array([10,255,255])

    cevir = cv2.cvtColor(goruntu,cv2.COLOR_BGR2HSV)

    donusturulengoruntu = cv2.inRange(cevir,reda,redb)

    cv2.imshow("kamera2",donusturulengoruntu)

    cv2.imshow("kamera",goruntu)

    if cv2.waitKey(30) and 0XFF == ("q"):
        break

kamera.release()

cv2.destroyAllWindows()