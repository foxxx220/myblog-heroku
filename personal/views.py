from django.shortcuts import render

def index(request):
	return render(request, "personal/home.html")

def contact(request):
	return render(request, "personal/contact.html", 
		{'contact': ['Phone: 97691220680', 'Address: Ulaanbaatar, Mongolia', 'E-mail: baterdene.tsogoo0220@gmail.com']})
