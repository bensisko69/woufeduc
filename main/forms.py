from django.forms import ModelForm, Textarea
from django_markdown.fields import MarkdownFormField
from django_markdown.widgets import MarkdownWidget
from django import forms
from .models import Contact, Presentation, Tarif, Temoignage, Partenaires, Gallery, Service, Mention

class ContactForm(ModelForm):
	class Meta:
		model = Contact
		exclude = ('validate',)
		widgets = {
			'question' : Textarea(attrs={'cols': 60, 'rows': 10}),
		}

class PresentationForm(ModelForm):
	class Meta:
		model = Presentation
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

class TemoignageForm(ModelForm):
	class Meta:
		model = Temoignage
		exclude = ('validate',)
		widgets = {
			'comment' : Textarea(attrs={'cols': 60, 'rows': 10}),
		}

class PartenairesForm(ModelForm):
	class Meta:
		model = Partenaires
		fields = '__all__'

class GalleryForm(ModelForm):
	class Meta:
		model = Gallery
		fields = '__all__'
		widgets = {
			'text' : Textarea(attrs={'cols': 60, 'rows': 10}),
		}

class ServiceForm(ModelForm):
	class Meta:
		model = Service
		fields = '__all__'
		widgets = {
			'left' : Textarea(attrs={'cols': 60, 'rows': 10}),
			'right' : Textarea(attrs={'cols': 60, 'rows': 10}),
		}

class MyCustomForm(forms.Form):
	content = forms.CharField(widget=MarkdownWidget())
	content2 = MarkdownFormField()

class MentionForm(ModelForm):
	class Meta:
		model = Mention
		fields = '__all__'
		widgets = {
			'text' : Textarea(attrs={'cols': 60, 'rows': 10}),
		}
