import numpy as np
import cv2 as cv
import bson
import base64
from bson.codec_options import CodecOptions
from bson.json_util import dumps

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    cv.imshow('direct_data', frame)
    encoded, buf= cv.imencode('.jpg', frame)
    image = base64.b64encode(buf)

    bbson = bson.BSON.encode({'shape': frame.shape, 'frame': image})

    payload = bson.BSON.decode(bbson)
    raw_image = base64.b64decode(payload['frame'])
    image = np.frombuffer(raw_image, dtype=np.uint8)
    frame=cv.imdecode(image,1)
    if cv.waitKey(20) & 0xFF == ord('d'):        # stop the video is the key 'd' is pressed (you can change as per your choice)
        break
