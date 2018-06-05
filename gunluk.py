from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
	#listele()
	#return app.send_static_file('index.html')
	return listele()
	
@app.route('/ekle')
def ekle():
	#return "burada ekleme yapicaz"
	return app.send_static_file('ekle.html')
	
@app.route('/listele')
def listele():
	#return "burada listeleme olacak hepsini"	
	con = sqlite3.connect('gunluk.db')
	c = con.cursor()
	c.execute('select id, tarih, baslik from gunluk order by id desc')
	data = c.fetchall()
	return render_template('listele.html', data=data)
	
@app.route('/read/<int:id>', methods=['GET'])
def read(id):
	if request.method == 'GET':
		con = sqlite3.connect('gunluk.db')
		c = con.cursor()
		c.execute("select * from gunluk where id = %d" % id)
		data = c.fetchall()
		return render_template('read.html', data=data)
	
@app.route('/add', methods=['POST'])
def add():
	if request.method == 'POST':
		tarih = request.form['tarih']
		baslik = request.form['baslik']
		icerik = request.form['icerik']
		icerik = icerik.replace('\n','<br>')
		
		
		#burada db islemleri yapicaz
		con = sqlite3.connect('gunluk.db')
		c = con.cursor()
		c.execute("insert into gunluk(tarih, baslik, icerik) values(?,?,?)", (tarih, baslik, icerik))
		con.commit()
		#return "basariyla eklendi<br><a href='/ekle'>yeni ekle</a> | <a href='/listele'>listele</a>"
		return listele()
		
if __name__ == "__main__":
	app.run()