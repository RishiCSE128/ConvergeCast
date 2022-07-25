from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/random/', methods=['POST'])
def hello_world():
    if request.method == 'POST':
        
        data=request.get_json(force=True)
        d = jsonify(data)
        print(d)
        return ('ok')

if __name__ == '__main__':
    app.run(host='10.33.16.19', port=5000)