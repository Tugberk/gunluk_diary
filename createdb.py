import sqlite3

con = sqlite3.connect('gunluk.db')

c = con.cursor()
c.execute("create table gunluk(id INTEGER PRIMARY KEY AUTOINCREMENT, tarih datetime, baslik TEXT, icerik TEXT)")