# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 14:04:24 2021

@author: moeez
"""

import cv2
vidcap = cv2.VideoCapture('simple.mp4')
success, image = vidcap.read()
count = 1

while success:
  cv2.imwrite("photos/image_%d.jpg" % count, image)    
  success, image = vidcap.read()
  print('Saved image ', count)
  count += 1