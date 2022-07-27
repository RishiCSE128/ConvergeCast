#this is twice the size of the brute zipped file because I used the based64 encoding 

import zlib, json, base64



ZIPJSON_KEY = 'base64(zip(o))'

def json_zip(j):


    j = {
        ZIPJSON_KEY: base64.b64encode(
            zlib.compress(
                json.dumps(j).encode('utf-8')
            )
        ).decode('ascii')
    }


<<<<<<< HEAD
    return(j)
=======
    return(j)
    
>>>>>>> 3d73d2af84c4e304c0073f8b524a6d7eea554ca9
