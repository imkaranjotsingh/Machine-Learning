'''
Created on Jan 10, 2017

@author: hanif
'''
from werkzeug.utils import secure_filename
import datetime
import cv2
import time
import os,sqlite3,hashlib
from module.Database import dba
from flask import Flask, flash, render_template, redirect, url_for, request, session

db = dba()

app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"
UPLOAD_FOLDER = 'static/images'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index1():
    #data = db.read(None)
    return render_template('index1.html',data = data)

#uploading image process
@app.route('/img',methods = ['POST' , 'GET'])
def img():
    camera_port = 0
    camera = cv2.VideoCapture(camera_port)
    time.sleep(1)
    return_value, image = camera.read()
    path = "static/images/1.jpg"
    cv2.imwrite(path, image)
    del(camera)
    imageName =  path[14:]
    print(imageName)
    imagename = imageName
    print(imagename)
    if db.insert_item(imagename):
        flash("A new product have been added!!!!")
    else:
        flash("A product cannot be added!!!")
    data = db.image_get(imagename)
    print(data)
    return render_template('image.html',data = data)

	
@app.route('/update/<int:id>/')
def update(id):
    data = db.read(id);
    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['update'] = id
        return render_template('update.html', data = data)


@app.route('/updatephone', methods = ['POST'])
def updatephone():
    if request.method == 'POST' and request.form['update']:
        if db.update(session['update'], request.form):
            flash('updated')
        else:
            flash('can not be updated')
        
        session.pop('update', None)
        
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/button/')
def button():
    return render_template('button.html')

@app.route('/image/')
def image():
    return render_template('image.html')

    #return render_template('image.html',data = data)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug = True, port=8181, host="0.0.0.0")
