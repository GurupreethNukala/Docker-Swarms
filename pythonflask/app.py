from flask import Flask
import logging

app = Flask(__name__)

logging.basicConfig(filename='/tmp/logs/basic_app.log',level=logging.DEBUG,format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

@app.route('/')
def welcome():
    return "Welcome to our python application running on docker"

@app.route('/hello')
def wish():
    return "Hello Members..Merry Christmas"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)
