from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
	return  HttpResponse('This is the  Homepage')

def abts(request):
	return  HttpResponse("<h2 style='background-color:green;color:white;padding:3px;margin-left:230px;margin-right:230px'>This is AboutPage</h2>")

def ruthu(self,name):
	return HttpResponse("<h2>Hi welcome {}</h2>".format(name))	

def table(request,y):
	j = ""
	for m in range(1,11):
		j += "{} X {:02} = {:02}".format(y,m,y*m)+"<br/>"
		print(j)
	return HttpResponse(j)

def rcds(request,name,age):
	#print(name,age)
	return render(request,'fy/userdt.html',{'n':name,'a':age})


def sample(request):
	return render(request,'fy/demo.html')