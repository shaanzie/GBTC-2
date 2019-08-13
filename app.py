import requests
import flask
import json
import subprocess
import os
from flask_cors import CORS
import threading
app = flask.Flask(__name__)
jsonData = ''
CORS(app)

#1
@app.route('/api/v1/create',methods= ['POST'])
def createContract():
    ''' creates vote contract '''
    cid=flask.request.json['candidate-id']
    #C:\Users\anand\Documents\GBTC\azure-vote\node_modules\.bin\wdio
    os.system(r".\\azure-vote\\node_modules\\.bin\\wdio .\\azure-vote\\wdio.conf.js --suite first")
    return flask.Response(status=201)

@app.route('/api/v1/action',methods=['GET'])
def takeaction():
    ''' does verification '''
    #profile values send as cli arguments
    trace="hello"
    os.system('../server/azurevote/node_modules/.bin/wdio wdio.conf.js --suite action '+trace)
    return flask.Response(status=200)

@app.route('/api/v1/verify',methods=['GET'])
def verify():
    ''' verfies whether the vote is valid '''
    os.system('../server/azurevote/node_modules/.bin/wdio wdio.conf.js --suite verify > verify.txt')
    #check if tests passed
    if(test):
        return flask.Response(status=200)
    else:
        return flask.Response(status=401)

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000)
