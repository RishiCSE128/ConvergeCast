# need for pilor interation https://www.cherryservers.com/blog/introduction-to-gpu-programming-with-cuda-and-python
# cuda reshape https://docs.cupy.dev/en/stable/reference/generated/cupy.reshape.html#cupy.reshape
# https://towardsdatascience.com/heres-how-to-use-cupy-to-make-numpy-700x-faster-4b920dda1f56
# https://towardsdatascience.com/python-performance-and-gpus-1be860ffd58d

from decomp import json_unzip
import cv2 as cv
import numpy as np
import json
import time
import numba
#import cupy as cp
from numba import jit, cuda
import base64
import bson
                         
@jit
def func2(b): 
   frame1 = np.asarray(json.loads(b['frame']),     dtype='uint8'                    ).reshape(b['shape'])
  
   return frame1

def repicture(c):
    raw_image = base64.b64decode(bson.loads(c['frame']))
    image = np.frombuffer(raw_image, dtype=np.uint8)
    frame = cv.imdecode(image, 1)
    a=json_unzip(j)
    #print(a)
    b=json.loads(a)
    frame1=func2(b)
    cv.imshow('test', frame)
    #if cv.waitKey(20) & 0xFF == ord('d'):    # stop the video is the key 'd' is pressed (you can change as per your choice)
     #   break

time.sleep(5)