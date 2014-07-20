# -*- coding: utf-8 -*- 

from django.db import models
from datetime import date

class Book(models.Model):
	BUTTON_TYPES = [(1, u'Прочитанное'), (2, u'Читаю'), (3, u'Хочу прочитать')]

	author = models.CharField(max_length=200,  verbose_name=u'Автор')
	title = models.CharField(max_length=200, verbose_name=u'Название книжки')
	book_pic = models.ImageField(upload_to="books/", default='books/nopic.jpg', verbose_name=u'Изображение')
	favorite = models.BooleanField(default='False', verbose_name=u'В избранном')
	action = models.IntegerField(choices=BUTTON_TYPES, default=1, verbose_name=u'Действие')
	date_reading = models.DateField(verbose_name=u'Дата прочтения', default=date.today)
	review = models.TextField(verbose_name=u'Отзыв', default='')

	def __unicode__(self):
		return u"{0} ({1})".format(self.author, self.title)

	class Meta:
		verbose_name = "книжку"
		verbose_name_plural = "книжка"