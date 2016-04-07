from django.db import models
from django_markdown.models import MarkdownField
# Create your models here.

NAME_PAGE = (
	('education', 'education'),
	('reeducation', 'reeducation'),
	('promenade', 'promenade'),
	)

class Contact(models.Model):
	prenom = models.CharField(max_length=100)
	nom = models.CharField(max_length=100)
	email = models.EmailField(max_length=50)
	codePostal = models.CharField(max_length=5)
	telephone = models.CharField(max_length=10)
	question = models.CharField(max_length=300)
	validate = models.BooleanField(default=False)

	def __str__(self):
		return self.nom

	def __unicode__ (self):
		return self.nom

class Presentation(models.Model):
	left = models.CharField(max_length=900)
	right = models.CharField(max_length=900)
	file1 = models.FileField(upload_to='main/static/img/presentation')
	file2 = models.FileField(upload_to='main/static/img/presentation')

class Tarif(models.Model):
	titre = models.CharField(max_length=100)
	detail = models.CharField(max_length=600)
	prix = models.IntegerField()

	def __str__(self):
		return self.titre

	def __unicode__ (self):
		return self.titre

class Temoignage(models.Model):
	titre = models.CharField(max_length=100)
	nom = models.CharField(max_length=100)
	comment = models.CharField(max_length=600)
	file = models.ImageField(upload_to='main/static/img/temoignage', blank=True, default='main/static/img/temoignage/img1.jpeg')
	validate = models.BooleanField(default=False)

	def __str__(self):
		return self.nom

	def __unicode__(self):
		return self.nom

class Partenaires(models.Model):
	file = models.ImageField(upload_to='main/static/img/partenaires')
	lien = models.CharField(max_length=250)
	nom = models.CharField(max_length=250)

	def __str__(self):
		return self.nom

	def __unicode__(self):
		return self.nom

class Gallery(models.Model):
	nom = models.CharField(max_length=100)
	file = models.ImageField(upload_to='main/static/gallery/')
	text = models.CharField(max_length=250)

	def __str__(self):
		return self.nom

	def __unicode__(self):
		return self.nom

class Text(models.Model):
	page = models.CharField(choices=NAME_PAGE, max_length=100)
	left = models.CharField(max_length=900)
	right = models.CharField(max_length=900)
	file1 = models.FileField(upload_to='main/static/img/text')
	file2 = models.FileField(upload_to='main/static/img/text')

	def __str__(self):
		return self.page

	def __unicode__(self):
		return self.page