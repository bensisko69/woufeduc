from django.contrib import admin
from django.db import models

from .models import Contact, Text, Tarif
from .forms import ContactForm, TextForm, TarifForm

class ContactAdmin(admin.ModelAdmin):
	form = ContactForm
	list_display = ('nom', 'codePostal', 'telephone')

class TextAdmin(admin.ModelAdmin):
	form = TextForm

class TarifAdmin(admin.ModelAdmin):
	form = TarifForm

admin.site.register(Contact, ContactAdmin)
admin.site.register(Text, TextAdmin)
admin.site.register(Tarif, TarifAdmin)