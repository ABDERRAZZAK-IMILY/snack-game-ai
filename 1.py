import cv2
import cvzone
import random
import math

from cvzone.HandTrackingModule import HandDetector


cap = cv2.VideoCapture(0)

cap.set(3,800)
cap.set(4,600)

while True:
    ok , img = cap.read()

    img = cv2.flip(img,1)
    cv2.imshow("snack game [python ai]" , img)

