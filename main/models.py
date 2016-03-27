from django.db import models
from django_markdown.models import MarkdownField
# Create your models here.

NAME_PAGE = (
	('acceuil', 'acceuil'),
	('presentation', 'presentation'),
	('education', 'education'),
	('tarifs', 'tarifs'),
	('contact', 'contact')
	)

class Contact(models.Model):
	prenom = models.CharField(max_length=100)
	nom = models.CharField(max_length=100)
	email = models.EmailField(max_length=50)
	codePostal = models.CharField(max_length=5)
	telephone = models.CharField(max_length=10)
	question = models.CharField(max_length=300)

	def __str__(self):
		return self.nom

	def __unicode__ (self):
		return self.nom

class Text(models.Model):
	page = models.CharField(max_length=200, choices=NAME_PAGE)
	left = models.CharField(max_length=900)
	right = models.CharField(max_length=900)

	def __str__(self):
		return self.page

	def __unicode__ (self):
		return self.page

class Tarif(models.Model):
	titre = models.CharField(max_length=100)
	detail = models.CharField(max_length=600)
	prix = models.IntegerField ()
	file = models.FileField(upload_to='main/static/img')

	def __str__(self):
		return self.titre

	def __unicode__ (self):
		return self.titre