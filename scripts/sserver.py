import cv2 as cv
import numpy as np
import time
import json
from json import JSONEncoder
from compress_json import json_zip
import requests
import base64




class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)
    
def gen_frames(fps):
    headers = {'Content-type': 'application/json'}
    video_location=0
    #counter = 0
    capture = cv.VideoCapture(video_location)
    try:
        while True:
            #print(f'sent frame {counter}')
            
            isTrue, frame = capture.read()
            #if cv.waitKey(20) & 0xFF == ord('d'):
                #break
            res = frame.shape
            print(frame)
            #frame = np.random.randint(256, size=res, dtype='uint8')
            #time.sleep(1/fps)
            #print(frame)
            img= base64.b64encode(frame)
           
            print (img)
            
            img1=np.frombuffer(base64.b64decode(img))
            print(img1)
           
             
            #paylaod_tx = json.dumps({'shape':res, 'frame':json.dumps(frame,cls=NumpyArrayEncoder)}) #each pixel will have a rgb color and the color will be stored into a matrix, each matrix will store a row
            payload = json.dumps({'shape':res, 'frame':json.dumps(frame,cls=NumpyArrayEncoder)})
            payload_tx=json_zip(payload)
            print(payload_tx)
       
            #print(time.time())
            response = requests.post("http://10.33.16.19:5000/server",data=payload_tx,headers=headers)
                        
            
            
            #counter += 1
    except(KeyboardInterrupt):
        print('released....')
        capture.release()
        
    
        #a=json_zip(paylaod_tx)
        #print(a)
        
        #requests.port(,data=a)

        
        
 
def main():
   
    fps=60
    gen_frames(fps)

main()
