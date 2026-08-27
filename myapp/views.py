from django.shortcuts import render, redirect
from myapp.models import RandomQuotes
from django.http import HttpResponse
from django.core.cache import cache
from datetime import datetime, timedelta
import requests
import json
# Create your views here.

def set_quote():
    now = datetime.now()
    seconds = (24*60*60) - (now.hour*60*60 + now.minute*60 + now.second)
    quote = RandomQuotes.objects.order_by('?').first()
    cache.set('quote_of_the_day', quote, timeout=seconds)

def get_quote():
    quote_of_the_day = cache.get('quote_of_the_day')

    if not quote_of_the_day:
        set_quote()
        quote_of_the_day = cache.get('quote_of_the_day')

    return quote_of_the_day

def index(request):
	quote_of_the_day = get_quote()
	return render(request, 'index.html',{'author': quote_of_the_day.author,'quote': quote_of_the_day.content})

def save(request):
	url = "https://dummyjson.com/quotes"
	response = requests.get(url)
	if response.status_code == 200:
		data = response.json()
		for x in data['quotes']:  # Access the 'quotes' list in the JSON response
				instance = RandomQuotes(
					author=x['author'],
					content=x['quote'],
				)
				instance.save()  # Save the instance to the database
		return HttpResponse('Quotes fetched and saved successfully')
	else:
		return HttpResponse(f'Failed to fetch quotes, status code: {response.status_code}')


def find(request):
	quote_of_the_day = get_quote()
	if request.method=="POST":
		name=request.POST.get('author_name')
		if name:
			data=name.title()
			quote= RandomQuotes.objects.filter(author=data)
			if quote.exists():
				r_quote = quote.first()
				return render(request,'index.html',{'author':r_quote.author, 'quote': r_quote.content})
			else:
				msg="author not found"
				return render(request, 'index.html', {'author':quote_of_the_day.author,'quote':quote_of_the_day.content,'msg1':msg})
		else:
			msg="enter author name"
			return render(request, 'index.html', {'author':quote_of_the_day.author,'quote':quote_of_the_day.content,'msg2':msg})
	else:
		return render(request,'index.html',{'author':quote_of_the_day.author,'quote':quote_of_the_day.content})

def refresh(request):
	quote = RandomQuotes.objects.order_by('?').first()
	return render(request, 'index.html', {'author': quote.author, 'quote': quote.content})

