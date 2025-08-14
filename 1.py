import cv2
import cvzone
import random
import math

from cvzone.HandTrackingModule import HandDetector


cap = cv2.VideoCapture(0)

cap.set(3,800)
cap.set(4,600)

detector = HandDetector(detectionCon=0.7 , maxHands=1)

while True:
    ok , img = cap.read()

    img = cv2.flip(img,1)

    hands , img = detector.findHands(img , flipType=False)

    cv2.imshow("snack game [python ai]" , img)

    key = cv2.waitKey(1)

