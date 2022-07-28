<<<<<<< HEAD
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
=======
#https://github.com/jar-o/flask-bson/pull/1/files

from flask import Flask, request, Response, session
import numpy as np
import time 
import cv2 as cv
import json 
from json import JSONEncoder
from decomp import json_unzip
import flask
from compress_json2 import repicture
import bson
import base64
from pymongo import MongoClient
from compress import image
import gc
import os
from os import environ
import threading
import socket
import requests
import subprocess

#from flask_bson import accept_bson, bsonify

app = Flask(__name__)




class TheClass:
    def hello_world(self,ipaddress):
        time.sleep(4)              
        environ["QT_DEVICE_PIXEL_RATIO"] = "0"
        environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
        environ["QT_SCREEN_SCALE_FACTORS"] = "1"
        environ["QT_SCALE_FACTOR"] = "1"
        #session['ax']=42
        t = time.time()
        while True:
            print(t)
            data= requests.get(f'http://{ipaddress}:5000/video')
            #data=request.data()
            #a=data.read()
            #print(a)
            print(t)
            print(data)
            #payload_rx=json.loads(data)
            #print(dd)
            
            #ses=a['ipadress']

            #print(ses)
            #a=bson.BSON(data).decode()
            #print(a)
            # raw_image = base64.b64decode(data['frame'])
            # print(raw_image)
            # image = np.frombuffer(data['frame'], dtype=np.uint8)
            # print(image)
            # frame = cv.imdecode(image, 1)
            #print(frame)
            #print(frame)
            # frame = np.asarray(
            #     json.loads(payload_rx['frame']), 
            #     dtype='uint8'
            # ).reshape(payload_rx['shape'])
            
            
            #cv.imshow('test', frame)

            #threading.Thread(target=imgshow(frame))
            print(t)
            #if cv.waitKey(20) & 0xFF == ord('d'):        # stop the video is the key 'd' is pressed (you can change as per your choice)
             #   break

            #session['ax']+=1
            #status_code = 200
            # del(frame)
            # gc.collect()

    # def imgshow(ff):      
    #     cv.imshow('test', ff)
    #     cv.waitKey(0)
    #     cv.destroyAllWindows()


@app.route('/server/',methods=['POST'])
def connect():
    if request.method == 'POST':
        data=request.data
        a=bson.BSON(data).decode()
        print(a)
        b=a['ipaddress']
        print(b)
        t= TheClass()
        threading.Thread(target=t.hello_world,args=(b,)).start()
        #t.start()
        #threading.Thread(target=TheClass.hello_world,args=(b,)).start()
    return("OK")


#@accept_bson(require_bson=True)
# @app.route('/response/', methods=['POST'])
# def response():
#     if request.method=='GET':
#         return(200)


if __name__ == '__main__':
    #from waitress import serve
    host = socket.gethostname()
    ipaddress =socket.gethostbyname(host)
<<<<<<< HEAD
    app.run(host='192.168.1.207', port=5000)
>>>>>>> 3d73d2af84c4e304c0073f8b524a6d7eea554ca9
=======
    #ip=subprocess.call(["./net.sh"])
    #ip=os.system("./scripts/net.sh")
    #print(ip)
    app.run(host='10.33.16.19', port=5000)
>>>>>>> 9898dc73ef93567fd25c9e2fe644bdf66daff3b3
