import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8)
colorR = (255,0,255)
cx,cy, w,h = 100,100,200,200

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)
    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"]
        distance, info, img = detector.findDistance(lmList1[4], lmList1[8], img) # distance between index and thumb
        if distance < 30:
            cursor = lmList1[8] # (x,y)
            if (cx-w//2)<cursor[0]<(cx+w//2) and (cx-h//2)<cursor[1]<(cx+h//2):
                colorR = (0,255,0)
                cx, cy = cursor
            else:
                colorR = (255,0,255)
    cv2.rectangle(img, (cx-w//2,cy-h//2), (cx+w//2,cx+h//2), colorR, cv2.FILLED)
    cv2.imshow("Image", img)
    cv2.waitKey(1)

