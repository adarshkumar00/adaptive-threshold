import cv2
import numpy
img=cv2.imread("girl hat.jpg",0)
cv2.imshow("original image",img)
'''pic=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,2)
cv2.imshow("adaptive threshold",pic)
pic=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,2)
cv2.imshow("adaptive threshold gaussian",pic)'''
cv2.namedWindow("image")
def nothing(x):
    pass
cv2.createTrackbar("adjust pixels","image",0,255,nothing)
while 1:
    pixels=cv2.getTrackbarPos("adjust pixels","image")
    if pixels%2==1 and pixels>5:
        pic=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,pixels,2)
        cv2.imshow("adaptive threshold mean",pic)
        pic=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,pixels,2)
        cv2.imshow("adaptive threshold gaussian",pic)
    k=cv2.waitKey(10) & 0xff
    if k==27:
        break
cv2.destroyAllWindows()
