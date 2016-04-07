from django.contrib import admin
from django.db import models

from .models import Contact, Presentation, Tarif, Temoignage, Partenaires, Gallery, Text
from .forms import ContactForm, PresentationForm, TarifForm, TemoignageForm, PartenairesForm, GalleryForm, TextForm

class ContactAdmin(admin.ModelAdmin):
	form = ContactForm
	list_display = ('nom', 'codePostal', 'telephone')
	list_filter = ['validate']

class PresentationAdmin(admin.ModelAdmin):
	form = PresentationForm

class TarifAdmin(admin.ModelAdmin):
	form = TarifForm

class TemoignageForm(admin.ModelAdmin):
	form = TemoignageForm
	list_filter = ['validate']

class PartenairesfAdmin(admin.ModelAdmin):
	form = PartenairesForm

class GalleryAdmin(admin.ModelAdmin):
	form = GalleryForm


class TextAdmin(admin.ModelAdmin):
	form = TextForm

admin.site.register(Temoignage, TemoignageForm)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Presentation, PresentationAdmin)
admin.site.register(Tarif, TarifAdmin)
admin.site.register(Partenaires, PartenairesfAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Text, TextAdmin)