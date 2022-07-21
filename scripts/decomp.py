import zlib, json, base64

ZIPJSON_KEY = 'base64(zip(o))'

def json_unzip(j, insist=True):
    try:
        assert (j[ZIPJSON_KEY])
        assert (set(j.keys()) == {ZIPJSON_KEY})
    except:
        if insist:
            raise RuntimeError("JSON not in the expected format {" + str(ZIPJSON_KEY) + ": zipstring}")
        else:
            return j

    try:
        j = zlib.decompress(base64.b64decode(j[ZIPJSON_KEY]))
    except:
        raise RuntimeError("Could not decode/unzip the contents")

    try:
        j = json.loads(j)
    except:
        raise RuntimeError("Could interpret the unzipped contents")

    print(j)



if __name__ == '__main__':
    j1=json.dumps({'base64(zip(o))': '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'})

    json_unzip(j1)