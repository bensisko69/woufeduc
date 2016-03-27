from django.shortcuts import render
from django.forms import forms
from django.core.mail import send_mail

from .forms import ContactForm
from .models import Text, Tarif

def accueil(request):
	obj = Text.objects.filter(page='acceuil')
	return render(request, 'main/acceuil.html', {'obj':obj})

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'main/acceuil.html')
	else:
		form = ContactForm()

	return render(request, 'main/contact.html', {'form':form})

def presentation(request):
	return render(request, 'main/presentation.html')

def education(request):
	obj = Text.objects.filter(page='education')
	return render(request, 'main/education.html', {'obj':obj})

def tarifs(request):
	obj = Tarif.objects.all()
	return render(request, 'main/tarifs.html', {'obj':obj})