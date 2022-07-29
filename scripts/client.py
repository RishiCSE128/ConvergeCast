from bz2 import compress
from ipaddress import ip_address
import zlib
import cv2 as cv
import base64
import bson
import requests
from flask import Flask, request, make_response, jsonify, Response, make_response
import json
from json import JSONEncoder
import numpy
import lz4
from bson.json_util import dumps, loads
import pickle

app = Flask(__name__)
#headers = {'Content-type': 'application/json'}
@app.route('/video/', methods=['GET'])
def video():
    #waith untill I get an other respinse
    capture= cv.VideoCapture(0)
    if request.method == 'GET':
        while True:
            isTrue, frame = capture.read()
            # cv.imshow('frame',frame)
            # if cv.waitKey(20) & 0xFF == ord('d'):
            #     break
            #print(frame.shape)
            encoded, buf =  cv.imencode('.jpg', frame)
            copress = zlib.compress(pickle.dumps(buf))
            #print(copress)
            #res= make_response()

            # img= base64.b64encode(buf)
            # a=bson.BSON.encode({'frame': img})
            #print(a)
            return Response(copress,status=200,headers={'Content':'B'})
 


if __name__ == '__main__':
    ip_address='10.33.16.17'
    ports=5000
    a=bson.BSON.encode({'ipaddress': ip_address, 'ports':ports})
    r=requests.post('http://10.33.16.19:5000/server',data=a)
    #print(r)
    app.debug=True
    app.run(host=ip_address,port=ports)
