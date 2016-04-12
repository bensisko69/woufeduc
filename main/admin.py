from django.contrib import admin
from django.db import models
from django_markdown.admin import MarkdownModelAdmin

from .models import Contact, Presentation, Tarif, Temoignage, Partenaires, Gallery, Service, MyModel, Mention
from .forms import ContactForm, PresentationForm, TarifForm, GalleryForm, ServiceForm, MentionForm

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
	form = PartenairesForm

class GalleryAdmin(admin.ModelAdmin):
	form = GalleryForm

class ServiceAdmin(admin.ModelAdmin):
	form = ServiceForm

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
