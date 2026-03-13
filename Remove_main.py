import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os
import PIL

cap = cv2.VideoCapture(0)
cap.set(3,48)
cap.set(4,48)
cap.set(cv2.CAP_PROP_FPS, 60)
segmentor = SelfiSegmentation()
fpsReader = cvzone.FPS
imgBg = cv2.imread("Images/Camera.png")

listImg = os.listdir("Resize images")
imgList  = []

for imgPath in  listImg:
      img = cv2.imread(f"Resize images/{imgPath}")
      imgList.append(img)
print(len(imgList))

indeximg = 0

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    imgOut = segmentor.removeBG(img,imgList[indeximg], threshold=0.5)

    imgStack = cvzone.stackImages([img, imgOut],2,1)
 #   frame, imgStack = fpsReader.update(imgStack, color=(0,0,255))
    cv2.imshow("Image", imgStack)
    key = cv2.waitKey(1)
    print(indeximg)
    if key == ord("a"):
          if indeximg>0:    
            indeximg -= 1
    elif key == ord("d"):
          if indeximg < len(imgList)-1:
            indeximg +=1
    elif key == ord("q"):
          break
