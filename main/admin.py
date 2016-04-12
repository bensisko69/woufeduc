from django.contrib import admin
from django.db import models
from django_markdown.admin import MarkdownModelAdmin

from .models import Contact, Presentation, Tarif, Temoignage, Partenaires, Gallery, Service, MyModel, Mention
from .forms import ContactForm, PresentationForm, TarifForm, TemoignageForm, PartenairesForm, GalleryForm, ServiceForm, MentionForm

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

class ServiceAdmin(admin.ModelAdmin):
	form = ServiceForm

# class MentionAdmin(admin.ModelAdmin):
	# form = MentionForm

admin.site.register(Temoignage, TemoignageForm)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Presentation, PresentationAdmin)
admin.site.register(Tarif, TarifAdmin)
admin.site.register(Partenaires, PartenairesfAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(MyModel, MarkdownModelAdmin)
# admin.site.register(Mention, MentionForm)