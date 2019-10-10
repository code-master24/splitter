from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.core.files.storage import FileSystemStorage
from .code import *
# Create your views here.
def index(request):
	temp1='splitter/sentence.html'
	temp2='splitter/output.html'
	if request.method == "POST":
		if request.POST.get('query2'):
			inp = request.POST.get('query2')
			out=sen(inp)
			print(out)
			return render(request,temp2,context={'out':out})
		elif request.FILES['query1']:
			myfile = request.FILES['query1']
			fs = FileSystemStorage()
			filename = fs.save(myfile.name, myfile)
			url = fs.url(filename)
			with open(url, 'r') as file:
				inp = file.read()
			print(inp)
			out=sen(inp)
			print(out)
			return render(request,temp2,context={'out':out})
	return render(request,temp1)

