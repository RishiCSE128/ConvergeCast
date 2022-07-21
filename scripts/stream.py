from re import I
import cv2 as cv
import numpy as np
import socket
import sys
import struct
import pickle

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect(('172.20.38.129',8008))

cam = cv.VideoCapture(0)


while True:
    rel,frame,data = cam.VideoCapture('./output2.mp4')
    data = pickle.dumps(data)

    message = struct.pack('L',len(data))

    clientSocket.sendall(message +data)