import cv2 as cv
import bson
import base64
import numpy as np
import time

def image(dd):
    while True:
        t= time.time()
        print(t)
        
        #print(dd)
        a=bson.BSON(dd).decode()
        #print(a)
        raw_image = base64.b64decode(a['frame'])
        #print(raw_image)
        image = np.frombuffer(raw_image, dtype=np.uint8)
        #print(image)
        frame = cv.imdecode(image, 1)
        print(frame)
        #a=json_unzip(j)
        #print(a)
        #b=json.loads(a)
        #frame1=func2(b)
        cv.imshow('test', frame)
        # print(t)
        # data1=request.get_json(force=True)
        # print(data1)
        # payload_rx = json.loads(data1)
        # frame1 = np.asarray(
        #             json.loads(payload_rx['frame']), 
        #             dtype='Binary'
        #         ).reshape(payload_rx['shape'])

        # cv.imshow('test', frame1)
        if cv.waitKey(20) & 0xFF == ord('d'):        # stop the video is the key 'd' is pressed (you can change as per your choice)
            break
        
        # return 'ok'
        # datadup=json.dumps(datanew)
        # data2=json_unzip(datadup)
        # print(data2)
        #data=json_unzip())   
        #print(data)