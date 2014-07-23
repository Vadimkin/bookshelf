# -*- coding: utf-8 -*- 
from __future__ import unicode_literals 
from __future__ import print_function
from bs4 import BeautifulSoup
import sqlite3 as lite
import MySQLdb
import urllib2
import re

#db = MySQLdb.connect(host="localhost", user="root", passwd="", db="zno", charset='utf8')
#cursor = db.cursor()

ACCOUNT = "vadimkin"
MONTHS = {'январь':'01', "февраль":'02', "март":'03', "апрель":'04', "май":'05', "июнь":'06', "июль":'07', "август":'08', "сентябрь":'09', "октябрь":'10', "ноябрь":'11', "декабрь": '12'}
ACTIONS = {'read':'1', 'now':'2', 'want':'3'}
con = None

con = lite.connect('db.sqlite3')
cur = con.cursor()    
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cur.fetchall())
cur.execute('PRAGMA table_info(`books_book`)')
print(cur.fetchall())
cur.execute('select * from `books_book`')
print(cur.fetchall())

for link, action in ACTIONS.items():
	read = urllib2.urlopen('http://bibla.ru/' + ACCOUNT + '/' + link + '/') .read()

	read_content = BeautifulSoup(read)
	read_content = read_content.find("ul", { "class" : "items" }).findAll("li", { "class" : "book" })

	for book in read_content:
		title = book.find("span", { "class" : "only-title" }).string
		try:
			pic = "http://bibla.ru" + book.find("div", { "class" : "poster" }).find("img")['src'].replace('thumbs/', '')
			pic_url = 'books/' + pic.split('/')[-1]
			f = open('i/'+pic.split('/')[-1], 'w+')
			f.write(urllib2.urlopen(pic) .read())
			f.close()
		except:
			pic = ""
			pic_url = 'books/nopic.jpg'
		print(pic)
		
		author = book.find("h3", { "class" : "author" }).find('a').string
		if author:
			author = author.replace('\\\'', '"')
			author = author.replace('\'', '"')
		reading_date = book.find("div", { "class" : "content" }).find("div", { "class" : "reading-times" }).string.strip()

		for month in MONTHS:
			if month in reading_date:
				reading_month = MONTHS[month]
				break

		reading_year = reading_date[-4:]
		reading_date = reading_year + "-" + reading_month + "-" + "01"

		try:
			note = book.find("div", { "class" : "content" }).find("div", { "class" : "note" }).renderContents()
		except:
			note = ""
		print(reading_date + ' = ' + str(reading_month) + ' ' + reading_year)
	#	query = u'INSERT INTO books_book(author, review, title, book_pic, date_reading, action) VALUES({0}, {1}, {2}, {3}, {4}, {5})'.format(str(author.decode('utf-8')),note.decode('utf-8'),title.decode('utf-8'),pic_url.decode('utf-8'),reading_date.decode('utf-8'),action)
		query = u'INSERT INTO books_book(author, review, title, book_pic, date_reading, action, favorite) VALUES(\'{0}\', \'{1}\', \'{2}\', \'{3}\', \'{4}\', \'{5}\', 0)'.format(author,note.decode('utf-8'),title,pic_url,reading_date,action)
		print(query)
		cur.execute(query)
		con.commit()

if con:
	cur.close()
	con.close()