import requests
import flask
import json
import subprocess
import os
from flask_cors import CORS
import threading
import smtplib
app = flask.Flask(__name__)
voteData=''
CORS(app)

#1
@app.route('/api/v1/create',methods= ['POST'])
def createContract():
    ''' creates vote contract '''
    global voteData
    cid=flask.request.json['candidateid']
    voteData=cid
    cid=cid.split()
    cid=''.join(cid)
    os.system(r".\\azure-vote\\node_modules\\.bin\\wdio .\\azure-vote\\wdio.conf.js --suite contract "+cid)
    return flask.Response(status=200)

@app.route('/api/v1/verify',methods=['GET'])
def takeaction():
    ''' does verification '''
    #profile values send as cli arguments
    trace=os.popen("python hashing.py").read()
    ver=os.system(r".\\azure-vote\\node_modules\\.bin\\wdio .\\azure-vote\\wdio.conf.js --suite verify "+trace)
    if ver!=0:
        return flask.Response(status=401)
    else:
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
        s.login("dummycred", "dummycred") 
        message = "Voted for "+voteData
        s.sendmail("dummysendcred", "dummyrecvcred", message) 
        s.quit() 
        return flask.Response(status=200)

@app.route('/api/v1/action',methods=['GET'])
def verify():
    ''' verfies whether the vote is valid '''
    os.system(r".\\azure-vote\\node_modules\\.bin\\wdio .\\azure-vote\\wdio.conf.js --suite action")
    return flask.Response(status=200)

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000)