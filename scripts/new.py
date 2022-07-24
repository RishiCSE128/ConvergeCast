import requests

r = requests.get("http://127.0.0.1:5000", data="Hey")

headers = {'ContentType':'application/json'}
frame = np.random.randint(256, size=res, dtype='uint8')
paylaod_tx = json.dumps({'shape':res, 'frame':json.dumps(frame,cls=NumpyArrayEncoder)}) #each pixel will have a rgb color and the color will be stored into a matrix, each matrix will store a row
request.post('http://192.168.207:500',json=payload,headers=headers)
