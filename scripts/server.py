import pickle
import socket
import struct
import cv2
import numpy as np
import json

#from scripts/decompressing import json_unzip

HOST = ''
PORT = 8008

def Server(username1, password1,ip1,endpoint1):
    username = username1
    password = password1
    ip=ip1
    endpoint =endpoint1
    video = cv2.CaptureVideo(f'rtsp://{username}:{password}@{ip}/{endpoint}')

    

    try:
        while True:
            ret, frame = video.read()
            cv2.imshow(f'Camera:{username}',frame)

            if cv2.waitKey(20) & 0xFF == ord('d'):        # stop the video is the key 'd' is pressed (you can change as per your choice)
                        break
            
            payload_rx = json.loads()

            frame1 = np.asarray(
                    json.loads(payload_rx['frame']), 
                    dtype='uint8'
                ).reshape(payload_rx['shape'])
        

    except Exception as e:
        print("ERROR:", e)

if __name__ == "__main__":
    # Release and close stream
    stream.release()
    cv2.destroyAllWindows()

    