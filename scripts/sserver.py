import re
from flask import Flask, request
import numpy as np
import numpy
import time 
import cv2 as cv
import json 
from json import JSONEncoder
from decomp import json_unzip
import flask
from compress_json2 import repicture


app = Flask(__name__)

@app.route('/server/',methods=['POST'])
def hello_world():

    while True:
        t = time.time()
        if request.method == 'POST':
            print(t)
            data1=request.get_json(force=True)
            print(data1)
            payload_rx = json.loads(data1)
            frame1 = np.asarray(
                        json.loads(payload_rx['frame']), 
                        dtype='uint8'
                    ).reshape(payload_rx['shape'])

            cv.imshow('test', frame1)
            if cv.waitKey(20) & 0xFF == ord('d'):        # stop the video is the key 'd' is pressed (you can change as per your choice)
                break
            
            return 'ok'
            # datadup=json.dumps(datanew)
            # data2=json_unzip(datadup)
            # print(data2)
            #data=json_unzip())   
            #print(data)
            

if __name__ == '__main__':
    app.run(host='192.168.1.207', port=5000)