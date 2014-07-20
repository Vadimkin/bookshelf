from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.conf import settings

import json

from books.models import Book

class IndexView(generic.ListView):
    template_name = 'books/index.html'

    def get_queryset(self):
    	return Book.objects.all()

class WantReadingView(generic.ListView):
    template_name = 'books/want.html'

    def get_queryset(self):
    	return Book.objects.all()

class NowReadingView(generic.ListView):
    template_name = 'books/now.html'

    def get_queryset(self):
    	return Book.objects.all()

class AjaxView(generic.View):
	def get(self, request, *args, **kwargs):
		book = Book.objects.get(id=kwargs['book_id'])
		if not book:
			return HttpResponse(json.dumps({'status':'error'}))
		result = {}
		result['status'] = 'ok'
		result['id'] = book.id
		result['author'] = book.author
		result['title'] = book.title
		result['pic'] = str(settings.MEDIA_URL) + str(book.book_pic)
		result['favorite'] = book.favorite
		result['date'] = str(book.date_reading)
		result['text'] = book.review

		return HttpResponse(json.dumps(result))