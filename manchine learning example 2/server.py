'''
Created on Jan 10, 2017

@author: hanif
'''
from werkzeug.utils import secure_filename
import datetime
import os,sqlite3,hashlib
import json
from module.Database import dba
from flask import Flask,jsonify, flash, render_template, redirect, url_for, request, session

db = dba()

app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index1():
    #data = db.read(None)
    return render_template('index1.html',data = data)

@app.route('/registration/')
def registration():
    return render_template('registration.html')

@app.route('/login/')
def login():
    return render_template('login.html')


@app.route('/admin/')
def admin():
    return render_template('admin.html')


@app.route('/invalid/')
def invalid():
    return render_template('invalid.html')

@app.route('/image/')
def image():
    return render_template('image.html')

@app.route('/salary/')
def salary():
    return render_template('salary.html')

@app.route('/ngoregister/')
def ngoregister():
    return render_template('ngoregister.html')

#uploading image process
@app.route('/img',methods = ['POST' , 'GET'])
def img():
    image = request.files['image']
    print(image)
    if image:
        filename = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        imagename = filename
        if db.insert_item(imagename ):
            flash("A new prodeuct have been added!!!!")
        else:
            flash("A product cannot be added!!!")
        return redirect(url_for('image'))
    else:
        return redirect(url_for('index'))
            

@app.route('/log',methods = [ 'POST' , 'GET'])
def log():
    if request.method == 'POST':
        n = db.check_login(request.form)
        a = ""
        if len(n) == 0:
            return redirect(url_for('registration'))
        for row in n:
            a = row[2]
        if a == 'admin':
            return redirect(url_for('admin'))
        elif a == 'customer':
            return redirect(url_for('customer'))
        else:
            return redirect(url_for('invalid'))
    else:
        return redirect(url_for('index'))

    
@app.route('/sal')
def sal():
    '''
    appDict = {
          'name': 'messenger',
          'playstore': True,
          'company': 'Facebook',
          'price': 100
    }
    '''
    name = []
    salary = []
    #data.append({'name': 'messenger','playstore': True,'company': 'Facebook','price': 100})
    n = db.read()
    if len(n) == 0:
        return None
    for row in n:
        a = row[1]
        b = row[2]
        name.append(a)
        salary.append(b)
    print(name)
    print(salary)
    return jsonify(name,salary)
  

@app.route('/delete/<int:id>/')
def delete(id):
    data = db.delete(id);
    return redirect(url_for('index'))
	
	
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

	

@app.route('/reg',methods = ['POST' , 'GET'])
def reg():
	if request.method == 'POST' :
		#amt = session['gross']
		if db.insert(request.form):
			flash("A new bill has been added")
		else:
			flash("A new bill can not be added")
            
		return redirect(url_for('registration'))
	else:
		return redirect(url_for('about'))

	    

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/blog/')
def blog():
    return render_template('blog.html')

@app.route('/blogsingle/')
def blogsingle():
    return render_template('blogsingle.html')

@app.route('/causes/')
def causes():
    return render_template('causes.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/donate/')
def donate():
    return render_template('donate.html')
@app.route('/customer/')
def customer():
    return render_template('customer.html')

@app.route('/event/')
def event():
    return render_template('event.html')

@app.route('/gallery/')
def gallery():
    return render_template('gallery.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug = True, port=8181, host="0.0.0.0")
