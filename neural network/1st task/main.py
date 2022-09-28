import cv2 as cv
import numpy as np

img = np.zeros((1024, 1024, 3), np.uint8)
vertices = np.array([[522, 256], [256, 600], [768, 600]], np.int32)
pts = vertices.reshape((-1, 1, 2))
cv.polylines(img, [pts], isClosed=True, color=(119, 221, 119), thickness=20)
cv.fillPoly(img, [pts], color=(50, 140, 50))

cv.ellipse(img, (522, 480), (120, 60), 0, 0, 360, (255, 255, 255), -1)
cv.circle(img, (522, 480), 55, (200, 0, 200), -1, cv.LINE_8)
cv.circle(img, (522, 480), 30, (0, 0, 0), -1, cv.LINE_8)

cv.putText(img, 'PurpleEye', (360, 700), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv.LINE_AA)
cv.line(img, (128, 780), (360, 780), (255, 255, 255), 2, cv.LINE_8)
cv.putText(img, 'by Ryuu', (400, 780), cv.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, (255, 255, 255), 2, cv.LINE_AA)
cv.line(img, (660, 780), (900, 780), (255, 255, 255), 2, cv.LINE_8)

cv.imshow('Text', img)
cv.waitKey(5000)
cv.destroyAllWindows()




