#to do: https://www.geeksforgeeks.org/running-python-script-on-gpu/

import numpy as np
import numpy
import time 
import cv2 as cv
import json 
from json import JSONEncoder
from compress_json import json_zip
from compress_json2 import repicture


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


def gen_frames(fps):   

    capture = cv.VideoCapture('./vids/Dota.mp4')   # reads the video into a capture object 

    while True:
        isTrue, frame = capture.read()
        #print(np.array(frame))
        #frame = np.random.randint(256, size=res, dtype='uint8')
        #time.sleep(1/fps)
        #print(frame)

        paylaod_tx = json.dumps({'shape':frame.shape, 'frame':json.dumps(np.array(frame),cls=NumpyArrayEncoder)}) #each pixel will have a rgb color and the color will be stored into a matrix, each matrix will store a row
        #paylaod_tx = json.dumps({'shape':res, 'frame':json.dumps(np.array(frame),cls=NumpyArrayEncoder)})
        zz=json_zip(paylaod_tx)
        #print(zz)
        repicture(zz)

        #payload_rx = json.loads(paylaod_tx) #this will go also to the server side
        #frame1 = np.asarray(
            #           json.loads(payload_rx['frame']), 
            #          dtype='uint8'
            #     ).reshape(payload_rx['shape'])


        # cv.imshow('test', frame1)
        
        if cv.waitKey(20) & 0xFF == ord('d'):    # stop the video is the key 'd' is pressed (you can change as per your choice)
            break
 
    
def main():
    res=(4,4,3)
    fps=60
    gen_frames(fps)

main()