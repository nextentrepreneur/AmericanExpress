from django.shortcuts import render
from django.http import HttpResponse
from . models import CreditCard
# Create your views here.
def index(request):
    return HttpResponse("Hello American Express")

def profile(request):
	'''
	if request.method == "GET":
		ID = request.GET.get("ID")
		user = CreditCard.objects.get(ID=ID)
		context = {"user":user}
		return render(request,'CreditCardStatement/profile.html',context)
    '''
	context = {}
	if request.method == "POST":
		ID = request.POST.get("ID")
		user = CreditCard.objects.get(ID=ID)
		context = {"user":user}
	return render(request,'CreditCardStatement/profile.html',context)
	