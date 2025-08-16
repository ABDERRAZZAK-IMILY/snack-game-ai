import cv2
import cvzone
import random
import math
from cvzone.HandTrackingModule import HandDetector


cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

detector = HandDetector(detectionCon=0.7, maxHands=1)


class SnackGame:
    def __init__(self):
        self.points = []
        self.lengths = []
        self.currentLength = 0
        self.allowedLength = 250
        self.previousHead = (0, 0)

    def update(self, imgMain, currentHead):
        px, py = self.previousHead
        cx, cy = currentHead

    
        self.points.append([cx, cy])
        distance = math.hypot(cx - px, cy - py)
        self.lengths.append(distance)
        self.currentLength += distance

    
        self.previousHead = (cx, cy)

        
        if len(self.points) > 1:
            for i in range(1, len(self.points)):
                cv2.line(imgMain, self.points[i - 1], self.points[i], (0, 0, 255), 20)

    
        if self.points:
            cv2.circle(imgMain, self.points[-1], 20, (200, 0, 200), cv2.FILLED)

        return imgMain


game = SnackGame()

while True:
    ok, img = cap.read()
    if not ok:
        break

    img = cv2.flip(img, 1)

    hands, img = detector.findHands(img, flipType=False)

    if hands:
        lmList = hands[0]['lmList']
        pointIndex = lmList[8][0:2]
        img = game.update(img, pointIndex)

    cv2.imshow("Snack Game [Python AI]", img)

    key = cv2.waitKey(1)
    if key == 27: 
        break

cap.release()
cv2.destroyAllWindows()
