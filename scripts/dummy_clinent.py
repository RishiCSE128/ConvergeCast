#to do: https://www.geeksforgeeks.org/running-python-script-on-gpu/
# import bson.codec_options https://pymongo.readthedocs.io/en/stable/api/bson/index.html to have better performance
#https://stackoverflow.com/questions/19877903/using-mongo-with-flask-and-python python with flask bson
import socket 
import cv2 as cv
import json 
from json import JSONEncoder
from compress_json import json_zip
<<<<<<< HEAD
import requests

=======
from compress_json2 import repicture
import base64
import bson
from bson.codec_options import CodecOptions
from bson.json_util import dumps
>>>>>>> 3d73d2af84c4e304c0073f8b524a6d7eea554ca9


def gen_frames(fps):   

    capture = cv.VideoCapture('./vids/Dota.mp4')   # reads the video into a capture object 

<<<<<<< HEAD
def gen_frames(fps, res):   
    try:
        #capture = cv.VideoCapture(0)
=======
    while True:
        isTrue, frame = capture.read()
        color = cv.cvtColor(frame, cv.COLOR_BGR2RGB) 
        #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        #print(np.array(frame))
        #print(np.array(gray))
        #frame = np.random.randint(256, size=res, dtype='uint8')
        #time.sleep(1/fps)
        #print(frame)
        #print(gray.shape)
        encoded, buf = cv.imencode('.jpg', color)
        image = base64.b64encode(buf)
        hostname = socket.gethostname()
        print (hostname)
        ipaddress= socket.gethostbyname(hostname)
        a=bson.BSON.encode({'shape': color.shape, 'frame': image, 'ipaddress': ipaddress})
        #payload= bson.BSON(a).decode()
        #print(payload)
        #a = bson.dumps({'shape': gray.shape, 'frame': image })
        #print(a)
        #paylaod_tx = json.dumps({'shape':gray.shape, 'frame':image}) #each pixel will have a rgb color and the color will be stored into a matrix, each matrix will store a row
        #paylaod_tx = json.dumps({'shape':res, 'frame':json.dumps(np.array(frame),cls=NumpyArrayEncoder)})
        #zz=json_zip(paylaod_tx)
        #print(zz)
        repicture(a)
>>>>>>> 3d73d2af84c4e304c0073f8b524a6d7eea554ca9

        #payload_rx = json.loads(paylaod_tx) #this will go also to the server side
        #frame1 = np.asarray(
            #           json.loads(payload_rx['frame']), 
            #          dtype='uint8'
            #     ).reshape(payload_rx['shape'])

<<<<<<< HEAD
            paylaod_tx = json.dumps({'shape':res, 'frame':json.dumps(frame,cls=NumpyArrayEncoder)}) #each pixel will have a rgb color and the color will be stored into a matrix, each matrix will store a row
            #paylaod_tx = json.dumps({'shape':res, 'frame':json.dumps(np.array(frame),cls=NumpyArrayEncoder)})
            a=json_zip(paylaod_tx)
            payload_rx = json.loads(paylaod_tx) #this will go also to the server side
=======
>>>>>>> 3d73d2af84c4e304c0073f8b524a6d7eea554ca9

        # cv.imshow('test', frame1)
        
        if cv.waitKey(20) & 0xFF == ord('d'):    # stop the video is the key 'd' is pressed (you can change as per your choice)
            break
 
    
def main():
    res=(4,4,3)
    fps=60
    gen_frames(fps)

main()