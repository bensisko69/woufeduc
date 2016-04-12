from django.contrib import admin
from django.db import models
from django_markdown.admin import MarkdownModelAdmin

from .models import Contact, Presentation, Tarif, Temoignage, Partenaires, Gallery, Service, MyModel, Mention
from .forms import ContactForm, TarifForm, MentionForm

class ContactAdmin(admin.ModelAdmin):
	model = Contact
	list_display = ('nom', 'codePostal', 'telephone')
	list_filter = ['validate']

class PresentationAdmin(admin.ModelAdmin):
	model = Presentation

class TarifAdmin(admin.ModelAdmin):
	form = TarifForm

class TemoignageAdmin(admin.ModelAdmin):
	model = Temoignage
	list_filter = ['validate']

class PartenairesfAdmin(admin.ModelAdmin):
	model = Partenaires

class GalleryAdmin(admin.ModelAdmin):
	model = Gallery

class ServiceAdmin(admin.ModelAdmin):
	model = Service

class MentionAdmin(admin.ModelAdmin):
	form = MentionForm

admin.site.register(Temoignage, TemoignageAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Presentation, PresentationAdmin)
admin.site.register(Tarif, TarifAdmin)
admin.site.register(Partenaires, PartenairesfAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(MyModel, MarkdownModelAdmin)
admin.site.register(Mention, MentionAdmin)
