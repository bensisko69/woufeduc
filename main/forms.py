from django.forms import ModelForm, Textarea

from .models import Contact, Presentation, Tarif, Temoignage, Partenaires, Gallery, Text

class ContactForm(ModelForm):
	class Meta:
		model = Contact
		fields = '__all__'
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
		fields = '__all__'
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

class TextForm(ModelForm):
	class Meta:
		model = Text
		fields = '__all__'
		widgets = {
			'left' : Textarea(attrs={'cols': 60, 'rows': 10}),
			'right' : Textarea(attrs={'cols': 60, 'rows': 10}),
		}