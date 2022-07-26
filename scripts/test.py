import cv2 as cv
import numpy as np


#video_location = 'output.mp4'   # specify the video location

try:
    capture = cv.VideoCapture('./vids/Dota.mp4')   # reads the video into a capture object 

    while True:
        isTrue, frame = capture.read()  # reads the video frame by frame, isTrue is boolean that stores the read status(boolean)
        cv.imshow(winname='Sample Video', mat=frame) # show images frame by frame 
        print (np.array(frame))
        print(frame.shape)
        if cv.waitKey(20) & 0xFF == ord('d'):        # stop the video is the key 'd' is pressed (you can change as per your choice)
            break
    capture.release()      # release the capture pointer
    cv.destroyAllWindows() # clear all memory resources  
except:
    print('Error !!')


def read_frame_as_jpg(in_filename, frame_num):
    out, err = (
        ffmpeg
        .input(in_filename)
        .filter_('select', 'gte(n,{})'.format(frame_num))
        .output('pipe:', vframes=1, format='image2', vcodec='mjpeg')
        .run(capture_stdout=True)
    )
    return out