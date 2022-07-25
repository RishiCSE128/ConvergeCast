globalvar=None

def put(frame1):
    global globalvar
    globalvar = frame1

def get():
    return globalvar