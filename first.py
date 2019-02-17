import numpy as np
import cv2

# img = np.zeros((100,100,3))
img = np.full((100,100), 0, dtype=int)
print(img)

img2 = np.random.rand(100,100,3)
print(img2)

img3 = cv2.imread("./sky.jpg")
img4 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
cv2.imshow("img", img)
# cv2.imshow("img2", img2)
# cv2.imshow("img3", img3)
# cv2.imshow("img4", img4)


img5 = cv2.imread("./sky.jpg")


cv2.waitKey(0)
