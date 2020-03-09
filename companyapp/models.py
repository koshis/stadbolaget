from django.db import models
from time import time
from ckeditor.fields import RichTextField
from django.utils.text import slugify


def generate_filename(instance, filename):
    ext = filename.split('.')[-1]
    return 'stuff_image/' + str(int(time())) + '.' + ext

class EntryQuerySet(models.QuerySet):
        def published(self):
            return self.filter(published=True)

class MenuItem(models.Model):
    menu=models.CharField(max_length=100)
    url = models.SlugField(unique=True)
    Descripton=RichTextField()
    order = models.PositiveSmallIntegerField(default=0, help_text='The order of the menu determines where this menu appears alongside other menus.')
    hassidemenu=models.BooleanField(default=True, help_text="if True page includes side menu")
    published=models.BooleanField(default=False)
    faicon=models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    objects = EntryQuerySet.as_manager()

    def __str__(self):
        return self.menu
    class Meta:
        verbose_name="Menu"
        verbose_name_plural="Menus"
        ordering=["-order"]

    def save(self, *args, **kwargs):
        self.url = self.url or slugify(self.menu)
        super().save(*args, **kwargs)
    def get_absolute_url(self):
                return "/kategori/%s/" % self.menu


class Menucategory(models.Model):
    menu=models.ForeignKey(MenuItem)
    name=models.CharField(max_length=100)
    Descripton=RichTextField()
    url = models.SlugField(unique=True)
    order = models.PositiveSmallIntegerField(default=0, help_text='The order of the menu determines where this menu appears alongside other menus.')
    hassidemenu=models.BooleanField(default=True, help_text="if True page includes side menu")
    published=models.BooleanField(default=False)
    faicon=models.CharField(max_length=100)
    created= models.DateTimeField(auto_now_add=True)

    objects=EntryQuerySet.as_manager()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name="Sub Menu"
        verbose_name_plural="Sub Menus"
        ordering=["-order"]

    def save(self, *args, **kwargs):
        self.url = self.url or slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
                return "/kategori/%s/" % self.name

class Messages(models.Model):
    Name = models.CharField(max_length=200,error_messages={'blank' : 'BLANK','required' : 'REQUIRED'})
    Location = models.CharField(max_length=200)
    PhoneNumber=models.CharField( max_length= 15)
    Email= models.EmailField()
    Message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)







