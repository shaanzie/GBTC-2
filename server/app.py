import requests
import flask
import json
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
    os.system('../server/azurevote/node_modules/.bin/wdio wdio.conf.js --suite contract '+cid)
    return flask.Response(status_code=201)

@app.route('/api/v1/action',methods=['GET'])
def takeaction():
    ''' does verification '''
    #profile values send as cli arguments
    trace="hello"
    os.system('../server/azurevote/node_modules/.bin/wdio wdio.conf.js --suite action '+trace)
    return flask.Response(status_code=200)

@app.route('/api/v1/verify',methods=['GET'])
def verify():
    ''' verfies whether the vote is valid '''
    os.system('../server/azurevote/node_modules/.bin/wdio wdio.conf.js --suite verify > verify.txt')
    #check if tests passed
    if(test):
        return flask.Response(status_code=200)
    else:
        return flask.Response(status_code=401)

@app.route('/api/v1/users', methods = ['POST'])
def addUser():
	#if not flask.request.json or not 'title' in flask.request.json:
		#flask.abort(400)
	sem.acquire()
	global count 
	count +=1 
	sem.release()
	if type(flask.request.json) != type({}):
		flask.abort(400)
	if not 'username' in flask.request.json and not 'password' in flask.request.json:
		flask.abort(400)
	if not is_sha1(flask.request.json['password']):
		flask.abort(400)
	with open('../toor/user.json', 'r') as user:
		jsonData = json.load(user)
		if flask.request.json['username'] in jsonData:
			flask.abort(400)
	jsonData[flask.request.json['username']] = flask.request.json['password']
	with open('../toor/user.json', 'w') as user:
		json.dump(jsonData, user)
	return flask.Response(status=201)

#2
@app.route('/api/v1/users/<string:username>', methods = ['DELETE'])
def deleteUser(username):
	sem.acquire()
	global count 
	count +=1 
	sem.release()
	with open('../toor/user.json', 'r') as user:
		jsonData = json.load(user)
	if not username in jsonData:
		flask.abort(400)
	r = requests.delete('http://ec2-52-90-112-239.compute-1.amazonaws.com/api/v1/users/' + username)
	if r.status_code != 200:
		flask.abort(400)

	jsonData.pop(username)
	with open('../toor/user.json', 'w') as user:
		json.dump(jsonData, user)

	return flask.Response(status=200)

	#12
@app.route('/api/v1/users/login', methods = ['POST'])
def CheckUser():
	sem.acquire()
	global count 
	count +=1 
	sem.release()
	with open('../toor/user.json', 'r') as user:
		jsonData = json.load(user)
	if not flask.request.json['username'] in jsonData or not jsonData[flask.request.json['username']] == flask.request.json['password'] :
		flask.abort(400)
	#jsonArray = flask.request.json['username']
	return flask.Response(flask.request.json['username'], status=200)

#13
@app.route('/api/v1/users', methods = ['GET'])
def getUser():
	sem.acquire()
	global count
	count +=1
	sem.release()
	with open('../toor/user.json', 'r') as user:
		jsonData = json.load(user)
	userList = []
	for x in jsonData:
		userList.append(x)
	return flask.jsonify(userList)

@app.route('/api/v1/users/isexist/<string:username>', methods = ['GET'])
def isExist(username):
	sem.acquire()
	global count
	count +=1
	sem.release()
	with open('../toor/user.json', 'r') as user:
		jsonData = json.load(user)
	if username not in jsonData:
		flask.abort(400)
	return flask.Response(status = 200)


@app.route('/api/v1/_count', methods = ['DELETE'])
def resetCount():
	sem.acquire()
	global count
	count =0
	sem.release()
	return flask.Response(status = 200)

@app.route('/api/v1/_count', methods = ['GET'])
def getCount():
	sem.acquire()
	global count
	retArray = []
	retArray.append(count)
	sem.release()
	return flask.jsonify(retArray)

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=80)
