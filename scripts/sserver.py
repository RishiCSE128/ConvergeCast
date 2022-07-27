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
import socket
import requests

#from flask_bson import accept_bson, bsonify

app = Flask(__name__)


def hello_world(ipaddress):
    time.sleep(1)              
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"
    #session['ax']=42
    t = time.time()
    while True:
        data= requests.get(f'http://{ipaddress}:5000/get_frame',data)
        #data=request.data()
        print(t)
        #print(dd)
        a=bson.BSON(data).decode()
        print(a)
        #ses=a['ipadress']

        #print(ses)
        #raw_image = base64.b64decode(data['frame'])
        #print(raw_image)
        image = np.frombuffer(data['frame'], dtype=np.uint8)
        #print(image)
        frame = cv.imdecode(image, 1)
        #print(frame)
        #print(frame)
        
        cv.imshow('test', frame)

        #threading.Thread(target=imgshow(frame))
        print(t)
        if cv.waitKey(20) & 0xFF == ord('d'):        # stop the video is the key 'd' is pressed (you can change as per your choice)
            break

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
        data=request.data()
        a=bson.BSON(data).decode()
        threading.Thread(target=hello_world,args=a['ipadress']).start()
        return("Connect")

#@accept_bson(require_bson=True)

if __name__ == '__main__':
    #from waitress import serve
    host = socket.gethostname()
    ipaddress =socket.gethostbyname(host)
    app.run(host='192.168.1.207', port=5000)