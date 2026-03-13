import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os
import numpy as np

print("Starting Program...")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera Error")
    exit()

cap.set(3, 640)
cap.set(4, 480)

segmentor = SelfiSegmentation()

folderPath = "Resize images"

listImg = os.listdir(folderPath)
imgList = []

for imgPath in listImg:
    img = cv2.imread(os.path.join(folderPath, imgPath))
    if img is not None:
        img = cv2.resize(img, (640, 480))
        imgList.append(img)

print("Loaded images:", len(imgList))

indeximg = 0

print("Entering loop...")

while True:
    success, img = cap.read()

    if not success:
        print("Frame not received")
        continue

    img = cv2.flip(img, 1)
    img = cv2.resize(img, (640, 480))

    bg = imgList[indeximg]

    try:
        imgOut = segmentor.removeBG(img, bg, threshold=0.7)
    except Exception as e:
        print("Segmentation failed:", e)
        continue

    # SHOW ONLY OUTPUT (no stackImages)
    cv2.imshow("Output", imgOut)

    key = cv2.waitKey(1)

    if key == ord("a") and indeximg > 0:
        indeximg -= 1

    if key == ord("d") and indeximg < len(imgList) - 1:
        indeximg += 1

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
