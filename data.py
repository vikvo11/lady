from flask import Markup
def Version():
    version = [
        {
            'id': 1,
            'CAR_OWNER': 'CD21.1',
            'CRDS_OWNER': 'CD21.1',
            'STG_OWNER': 'CD21.1',
            'Instanse': 'PROD',
            'author': 'vorovik',
            'create_date': '03-01-2017'

        },
        {
            'id': 2,
            'CAR_OWNER': 'CD20.1',
            'CRDS_OWNER': 'CD20.1',
            'STG_OWNER': 'CD20.1',
            'Instanse': 'UAT',
            'author': 'vorovik',
            'create_date': '03-01-2017'
        }
    ]
	#source={'logo':'source/logo.png','block1':'img/05.jpg'}
    return version

def source():
    source={'logo':'source/logo.png','block1':'img/05.jpg'} #_block1.html
    return source
def header():
    header={'phone':'777-777-7777','email':'e-mail: info@ladymarlene.ru','link':'https://vk.com/ladymarlene','infolink':'vk.com/ladymarlene','city':'г. Москва'} #_header.html
    return header
def carousel_items():
    carousel_items=(
	{'id':1001,'img':'source/b02.png','b_img':'source/b02_big.png','price':'1300','link':'glasses'},
	{'id':1002,'img':'source/b03.png','b_img':'source/b03_big.png','price':'1400','link':'glasses'},
	{'id':1003,'img':'source/b04.png','b_img':'source/b04_big.png','price':'1500','link':'glasses'},
	{'id':1004,'img':'source/b05.png','b_img':'source/b05_big.png','price':'1600','link':'glasses'},
	{'id':1005,'img':'source/b06.png','b_img':'source/b06_big.png','price':'1100','link':'glasses'},
	{'id':1006,'img':'source/b07.png','b_img':'source/b07_big.png','price':'1600','link':'glasses'},
	{'id':1007,'img':'source/b08.png','b_img':'source/b08_big.png','price':'1200','link':'glasses'},
	{'id':1008,'img':'source/b01.png','b_img':'source/b01_big-1.png','price':'1900','link':'glasses'})#_glasses.html
    return carousel_items
def mob_menu():
    mob_menu={'pos0':'Меню'} #_h_menu.html
    return mob_menu	
def menu():
    menu={'main':'ГЛАВНАЯ','/glasses':'БОКАЛЫ','index.html#bottle':'БУТЫЛКИ','index.html#locks':'ЗАМОЧКИ','index.html#reviews':'ОТЗЫВЫ','index.html#work':'НАШИ РАБОТЫ','index.html#delivery':'ДОСТАВКА'} #_h_menu.html
    return menu
def block2():
    block2={'b2_title':'Сегодня никогда не повторится…','b2_text':Markup(u'''<p><em>Это тот день, который вы ждете с трепетом и будете вспоминать всю жизнь. Сохранить память об этом важном событии и создать оригинальный аксессуар праздничного дня можно с помощью гравировки на свадебных бокалах, бутылках и замочках. Мы с радостью поможем сделать главный день в вашей жизни оригинальным и незабываемым!</em></p>'''),'b2_text2':Markup(u'''<em> День вашей свадьбы должен быть особенным и оставить прекрасные воспоминания!</em></p>
<p style="text-align: center;"><em>Lady-MarLene оказывает услуги <strong>индивидуальной гравировки</strong>:</em><br />
<em> &#8212; на <strong>бокалах</strong> для молодоженов,</em><br />
<em> &#8212; на <strong>бутылках</strong> шампанского для дня свадьбы, в благодарность родителям, на первую годовщину и рождение первенца,</em><br />
<em> &#8212; на <strong>замочках</strong></em></p>
<p style="text-align: center;"><em>Мы любим и ценим свою работу, стараясь сделать ваш незабываемый день оригинальным!</em></p>''')} #_blokc2.html
    return block2
def cart_items():
    cart_items=(
	{'u_id':'10011','name':'name1','id':1001,'img':'source/shablon_5_mini.png','price':'1300','link':'glasses'},
	{'u_id':'10012','name':'name1','id':1001,'img':'source/shablon_6_mini.png','price':'1400','link':'glasses'},
	{'u_id':'10013','name':'name1','id':1001,'img':'source/shablon_11_mini.png','price':'1500','link':'glasses'},
	{'u_id':'10014','name':'name1','id':1001,'img':'source/shablon_27_mini.png','price':'1600','link':'glasses'},
	{'u_id':'10015','name':'name1','id':1001,'img':'source/shablon_29_mini.png','price':'1100','link':'glasses'},
	{'u_id':'10016','name':'name1','id':1001,'img':'source/shablon_49_mini.png','price':'1600','link':'glasses'},
	
	{'u_id':'10021','name':'name2','id':1002,'img':'source/shablon_5_mini.png','price':'1300','link':'glasses'},
	{'u_id':'10022','name':'name2','id':1002,'img':'source/shablon_6_mini.png','price':'1400','link':'glasses'},
	{'u_id':'10023','name':'name2','id':1002,'img':'source/shablon_11_mini.png','price':'1500','link':'glasses'},
	{'u_id':'10024','name':'name2','id':1002,'img':'source/shablon_27_mini.png','price':'1600','link':'glasses'},
	{'u_id':'10025','name':'name2','id':1002,'img':'source/shablon_29_mini.png','price':'1100','link':'glasses'},
	{'u_id':'10026','name':'name2','id':1002,'img':'source/shablon_49_mini.png','price':'1600','link':'glasses'},
	
	{'u_id':'10031','name':'name3','id':1003,'img':'source/shablon_5_mini.png','price':'1300','link':'glasses'},
	{'u_id':'10032','name':'name3','id':1003,'img':'source/shablon_6_mini.png','price':'1400','link':'glasses'},
	{'u_id':'10033','name':'name3','id':1003,'img':'source/shablon_11_mini.png','price':'1500','link':'glasses'},
	{'u_id':'10034','name':'name3','id':1003,'img':'source/shablon_27_mini.png','price':'1600','link':'glasses'},
	{'u_id':'10035','name':'name3','id':1003,'img':'source/shablon_29_mini.png','price':'1100','link':'glasses'},
	{'u_id':'10036','name':'name3','id':1003,'img':'source/shablon_49_mini.png','price':'1600','link':'glasses'},
	
	{'u_id':'10041','name':'name4','id':1004,'img':'source/shablon_5_mini.png','price':'1300','link':'glasses'},
	{'u_id':'10042','name':'name4','id':1004,'img':'source/shablon_6_mini.png','price':'1400','link':'glasses'},
	{'u_id':'10043','name':'name4','id':1004,'img':'source/shablon_11_mini.png','price':'1500','link':'glasses'},
	{'u_id':'10044','name':'name4','id':1004,'img':'source/shablon_27_mini.png','price':'1600','link':'glasses'},
	{'u_id':'10045','name':'name4','id':1004,'img':'source/shablon_29_mini.png','price':'1100','link':'glasses'},
	{'u_id':'10046','name':'name4','id':1004,'img':'source/shablon_49_mini.png','price':'1600','link':'glasses'},
	
	{'u_id':'10051','name':'name5','id':1005,'img':'source/shablon_5_mini.png','price':'1300','link':'glasses'},
	{'u_id':'10052','name':'name5','id':1005,'img':'source/shablon_6_mini.png','price':'1400','link':'glasses'},
	{'u_id':'10053','name':'name5','id':1005,'img':'source/shablon_11_mini.png','price':'1500','link':'glasses'},
	{'u_id':'10054','name':'name5','id':1005,'img':'source/shablon_27_mini.png','price':'1600','link':'glasses'},
	{'u_id':'10055','name':'name5','id':1005,'img':'source/shablon_29_mini.png','price':'1100','link':'glasses'},
	{'u_id':'10056','name':'name5','id':1005,'img':'source/shablon_49_mini.png','price':'1600','link':'glasses'},
	
	{'u_id':'10061','name':'name6','id':1006,'img':'source/shablon_5_mini.png','price':'1300','link':'glasses'},
	{'u_id':'10062','name':'name6','id':1006,'img':'source/shablon_6_mini.png','price':'1400','link':'glasses'},
	{'u_id':'10063','name':'name6','id':1006,'img':'source/shablon_11_mini.png','price':'1500','link':'glasses'},
	{'u_id':'10064','name':'name6','id':1006,'img':'source/shablon_27_mini.png','price':'1600','link':'glasses'},
	{'u_id':'10065','name':'name6','id':1006,'img':'source/shablon_29_mini.png','price':'1100','link':'glasses'},
	{'u_id':'10066','name':'name6','id':1006,'img':'source/shablon_49_mini.png','price':'1600','link':'glasses'},
	
	{'u_id':'10071','name':'name7','id':1007,'img':'source/shablon_5_mini.png','price':'1300','link':'glasses'},
	{'u_id':'10072','name':'name7','id':1007,'img':'source/shablon_6_mini.png','price':'1400','link':'glasses'},
	{'u_id':'10073','name':'name7','id':1007,'img':'source/shablon_11_mini.png','price':'1500','link':'glasses'},
	{'u_id':'10074','name':'name7','id':1007,'img':'source/shablon_27_mini.png','price':'1600','link':'glasses'},
	{'u_id':'10075','name':'name7','id':1007,'img':'source/shablon_29_mini.png','price':'1100','link':'glasses'},
	{'u_id':'10076','name':'name7','id':1007,'img':'source/shablon_49_mini.png','price':'1600','link':'glasses'},
	
	{'u_id':'10081','name':'name8','id':1008,'img':'source/shablon_5_mini.png','price':'1300','link':'glasses'},
	{'u_id':'10082','name':'name8','id':1008,'img':'source/shablon_6_mini.png','price':'1400','link':'glasses'},
	{'u_id':'10083','name':'name8','id':1008,'img':'source/shablon_11_mini.png','price':'1500','link':'glasses'},
	{'u_id':'10084','name':'name8','id':1008,'img':'source/shablon_27_mini.png','price':'1600','link':'glasses'},
	{'u_id':'10085','name':'name8','id':1008,'img':'source/shablon_29_mini.png','price':'1100','link':'glasses'},
	{'u_id':'10086','name':'name8','id':1008,'img':'source/shablon_49_mini.png','price':'1600','link':'glasses'})#_glasses.html
    return cart_items