import cv2
import numpy as np

n_r = 12
n_c = 15
imgname1 = 'image_1.jpg'
criteria = (cv2.TERM_CRITERIA_EPS|cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
img1 = cv2.imread(imgname1)
gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
ret1,corners1 = cv2.findChessboardCorners(gray1,(n_r,n_c),None)
if ret1:
    cv2.cornerSubPix(gray1,corners1,(11,11),(-1,-1),criteria)
    cv2.drawChessboardCorners(img1, (n_r,n_c), corners1,ret1)
    print corners1
cv2.imshow("1",img1);
cv2.imwrite("detect.jpg",img1)
cv2.waitKey(0)