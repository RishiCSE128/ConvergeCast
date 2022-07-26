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
from os import environ
import threading

#from flask_bson import accept_bson, bsonify

app = Flask(__name__)

@app.route('/server/',methods=['POST'])
#@accept_bson(require_bson=True)
def hello_world():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"
    #session['ax']=42
    t = time.time()
    while True:
        print(t)
        if request.method == 'POST':
            dd = request.data
            print(t)
            #print(dd)
            a=bson.BSON(dd).decode()
            #print(a)
            ses=a['ipadress']

            print(ses)
            raw_image = base64.b64decode(a['frame'])
            #print(raw_image)
            image = np.frombuffer(raw_image, dtype=np.uint8)
            #print(image)
            frame = cv.imdecode(image, 1)
            #print(frame)
            #print(frame)
            cv.imshow('test', frame)
            cv.waitKey(0)

            #threading.Thread(target=imgshow(frame))
    
            print(t)
            if cv.waitKey(20) & 0xFF == ord('d'):        # stop the video is the key 'd' is pressed (you can change as per your choice)
                break

            #session['ax']+=1
            #status_code = 200
            # del(frame)
            # gc.collect()
            return("Continue")

# def imgshow(ff):      
#     cv.imshow('test', ff)
#     cv.waitKey(0)
#     cv.destroyAllWindows()

if __name__ == '__main__':
    #from waitress import serve
    app.run(host='10.33.16.19', port=5000)