from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/random/', methods=['POST'])
def hello_world():
    if request.method == 'POST':
        data=request.get_json(force=True)
        print(data)
        return 'ok'

if __name__ == '__main__':
    app.run(host='192.168.1.207', port=5000)