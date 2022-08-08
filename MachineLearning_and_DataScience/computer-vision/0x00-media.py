#!/usr/bin/env python3
""" read image in grayscale"""
import cv2
import numpy as np

img = cv2.imread("./img/001.jpeg", 0)  # 0 means grayscale image when load, for local images
img2 = cv2.imread("./img/002.jpeg")
img2Gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)  # convert image to grayscale after read
cv2.imshow("color image", img2)
cv2.imshow("Grayscale image", img2Gray)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
