#import pymongo
#from pymongo import MongoClient
#import json
#import pymongo
#from bson import BSON
#from bson import json_util
from flask import Flask, flash, redirect, render_template, request, session, abort,url_for,logging,Markup #For work with HTTP and templates
import requests # For HTTP requests
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

#Dashbord
@app.route('/dashbord',methods=['GET','POST'])
def dashbord():
    msg = py()
    return render_template('dashbordpymongo.html', articles='test')

#Dashbord
@app.route('/main',methods=['GET','POST'])
def main():
    #msg = py()
    #return render_template('index.html')

	header={'phone':'777-777-7777','email':'e-mail: info@ladymarlene.ru','link':'https://vk.com/ladymarlene','infolink':'vk.com/ladymarlene','city':'г. Москва'} #_header.html
	source={'logo':'source/logo.png','block1':'img/05.jpg'} #_block1.html
	mob_menu={'pos0':'Меню'} #_h_menu.html
	menu={'home':'ГЛАВНАЯ','glasses':'БОКАЛЫ','bottle':'БУТЫЛКИ','locks':'ЗАМОЧКИ','reviews':'ОТЗЫВЫ','work':'НАШИ РАБОТЫ','delivery':'ДОСТАВКА'} #_h_menu.html
	block2={'b2_title':'Сегодня никогда не повторится…','b2_text':Markup(u'''<p><em>Это тот день, который вы ждете с трепетом и будете вспоминать всю жизнь. Сохранить память об этом важном событии и создать оригинальный аксессуар праздничного дня можно с помощью гравировки на свадебных бокалах, бутылках и замочках. Мы с радостью поможем сделать главный день в вашей жизни оригинальным и незабываемым!</em></p>'''),'b2_text2':Markup(u'''<em> День вашей свадьбы должен быть особенным и оставить прекрасные воспоминания!</em></p>
<p style="text-align: center;"><em>Lady-MarLene оказывает услуги <strong>индивидуальной гравировки</strong>:</em><br />
<em> &#8212; на <strong>бокалах</strong> для молодоженов,</em><br />
<em> &#8212; на <strong>бутылках</strong> шампанского для дня свадьбы, в благодарность родителям, на первую годовщину и рождение первенца,</em><br />
<em> &#8212; на <strong>замочках</strong></em></p>
<p style="text-align: center;"><em>Мы любим и ценим свою работу, стараясь сделать ваш незабываемый день оригинальным!</em></p>''')} #_blokc2.html
	
	
	return render_template('dashbord_lady.html', header=header,source=source,mob_menu=mob_menu,menu=menu,block2=block2)	
	
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
