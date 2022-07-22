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


    return(j)