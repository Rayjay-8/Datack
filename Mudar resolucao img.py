import cv2

src = cv2.imread("ll.png",cv2.IMREAD_UNCHANGED)
scale = 25
width = int(src.shape[1]*scale/100)
height = int(src.shape[0]*scale/100)

dsize = (width,height)
output = cv2.resize(src,dsize)
cv2.imwrite("ll2.png",output)
