#import pymongo
#from pymongo import MongoClient
#import json
#import pymongo
#from bson import BSON
#from bson import json_util
from flask import Flask, flash, redirect, render_template, request, session, abort,url_for,logging,Markup #For work with HTTP and templates
import requests # For HTTP requests
from data import source,header,mob_menu,menu,block2,carousel_items,cart_items
import json
#from functools import wraps # For lock access
#from HTTP_basic_Auth import auths # For lock access

#client = MongoClient("ds141786.mlab.com:41786", username = 'podarkin', password = 'podarkin', authSource = 'heroku_q51pzrtm')
#db = client["heroku_q51pzrtm"]
#bookings_coll = db.bookings

app = Flask(__name__)
app.config['SECRET_KEY'] = 'morkovka18'
#Check if user logged in
#def is_logged_in(f):
#    @wraps(f)
#    def wrap(*args,**kwargs):
#        if 'logged_in' in session:
#            return f(*args,**kwargs)
#        else:
            #flash('Unauthorized, Please login', 'danger')
#            return redirect(url_for('login'))
#    return wrap

#@app.route('/')
#@is_logged_in

def home():
    a=1
    return redirect(url_for('dashbord'))

'''
@app.route('/test1')
def test():
    msg = py()
    return render_template('home.html', articles=msg)
'''
#Logout
#Dashbord
@app.route('/dashbord1',methods=['GET','POST'])
def dashbord1():
    msg = py()
    return render_template('main.html', articles='test')
	
@app.route('/cart',methods=['GET','POST'])
def cart():
    
    return render_template('cart.html', header=header(),source=source(),mob_menu=mob_menu(),menu=menu(),block2=block2(),carousel_items=carousel_items(),cart_items=cart_items())
	
@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out','success')
    return redirect(url_for('login'))

#User Login
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        #Get Form fields
        username = request.form['username']
        password_candidate = request.form['password']
        #users=auths()
        if auths(username,password_candidate):
            session['logged_in']= True
            return redirect(url_for('dashbord'))
        else:
                error='Invalid login'
                return render_template('login.html',error=error)

    return render_template('login.html')
@app.route('/start', methods=['POST'])
def get_counts():
    # get url
    data = json.loads(request.data.decode())
    #print(data['data']['subTotal'])
    subTotal=data['data']['subTotal']
    url = '123' #data["tax"]
    if 'http://' not in url[:7]:
        url = 'http://' + url

    return str(subTotal)	
@app.route('/glasses',methods=['GET','POST'])
def glasses():
    item_id = request.args.get('item_id', default = 0, type = int)
    filter = request.args.get('filter', default = '*', type = str)
	#/my-route?page=10&filter=test   -> page: 10  filter: 'test'
	
    #item_id=0;
    if request.method == 'POST':
        #Get Form fields
        item_id = request.form['item_id']
        item_img = request.form['item_img']
        #users=auths()
	#print(data.header)
    return render_template('glasses.html', header=header(),source=source(),mob_menu=mob_menu(),menu=menu(),block2=block2(),carousel_items=carousel_items(),cart_items=cart_items(),item_id=item_id)

#Dashbord
@app.route('/dashbord',methods=['GET','POST'])
def dashbord():
    msg = py()
    return render_template('index.html', articles='test')

#Dashbord 
@app.route('/main',methods=['GET','POST'])
def main():
    #msg = py()
    #return render_template('index.html')
	
	return render_template('dashbord_lady.html', header=header(),source=source(),mob_menu=mob_menu(),menu=menu(),block2=block2(),carousel_items=carousel_items())	
	
def py():
    #client = MongoClient("ds141786.mlab.com:41786", username = 'podarkin', password = 'podarkin', authSource = 'heroku_q51pzrtm')
    #db = client["heroku_q51pzrtm"]
    #bookings_coll = db.bookings
    #doc = bookings_coll.find_one()
    #asa = json.dumps(doc, sort_keys=True, indent=4, default=json_util.default)
    #docs = bookings_coll.find()
    #id = docs[0]['name']
    #return docs
	return None

def main():
    #doc = bookings_coll.find_one()


    pass
   # a = [x for x in bookings_coll.find()]


if __name__ == '__main__':
	app.run(debug=True)
    #main()
