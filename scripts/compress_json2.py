from decomp import json_unzip
import cv2 as cv
import numpy as np
import json
import time
import numba
import cupy as cp
from numba import jit, cuda 

                         
@jit 
def func2(b): 
   frame1 = cp.asarray(json.loads(b['frame']),     dtype='uint8'                    ).reshape(b['shape'])
  
   return frame1

def repicture(c):
    j=c
    a=json_unzip(j)
    #print(a)
    b=json.loads(a)
    frame1=func2(b)
    cv.imshow('test', frame1)
    #if cv.waitKey(20) & 0xFF == ord('d'):    # stop the video is the key 'd' is pressed (you can change as per your choice)
     #   break

time.sleep(5)