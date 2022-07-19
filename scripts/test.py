import cv2 as cv

video_location = 'vids/sample1.mp4'   # specify the video location
try:
    capture = cv.VideoCapture(video_location)   # reads the video into a capture object 

    while True:
        isTrue, frame = capture.read()  # reads the video frame by frame, isTrue is boolean that stores the read status(boolean)
        cv.imshow(winname='Sample Video', mat=frame) # show images frame by frame 
        if cv.waitKey(20) & 0xFF == ord('d'):        # stop the video is the key 'd' is pressed (you can change as per your choice)
            break
    capture.release()      # release the capture pointer
    cv.destroyAllWindows() # clear all memory resources  
except:
    print('Error !!')