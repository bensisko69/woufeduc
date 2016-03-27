from django.forms import ModelForm, Textarea

from .models import Contact, Text, Tarif

class ContactForm(ModelForm):
	class Meta:
		model = Contact
		fields = '__all__'
		widgets = {
			'question' : Textarea(attrs={'cols': 60, 'rows': 10}),
		}

class TextForm(ModelForm):
	class Meta:
		model = Text
		fields = '__all__'
		widgets = {
			'left' : Textarea(attrs={'cols': 60, 'rows': 10}),
			'right' : Textarea(attrs={'cols': 60, 'rows': 10}),
		}


class TarifForm(ModelForm):
	class Meta:
		model = Tarif
		fields = '__all__'
		widgets = {
			'detail' : Textarea(attrs={'cols': 60, 'rows': 10}),
		}

