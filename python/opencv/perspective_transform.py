#!/usr/bin/python3
# This code is taken from OpenCV (https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_geometric_transformations/py_geometric_transformations.html)

import cv2
import numpy as np
from matplotlib import pyplot as plt

def main(image):
  img = cv2.imread(image)
  rows,cols,ch = img.shape

  pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
  pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

  M = cv2.getPerspectiveTransform(pts1,pts2)

  dst = cv2.warpPerspective(img,M,(300,300))

  plt.subplot(121),plt.imshow(img),plt.title('Input')
  plt.subplot(122),plt.imshow(dst),plt.title('Output')
  plt.show()
  
if __name__ == "__main__":
  image = str(input("Image to transform: "))
  main(image)
