from django.db import models
from time import time
from ckeditor.fields import RichTextField

def generate_filename(instance, filename):
    ext = filename.split('.')[-1]
    return 'stuff_image/' + str(int(time())) + '.' + ext

class EntryQuerySet(models.QuerySet):
        def published(self):
            return self.filter(has_level_two=True)

class MenuItem(models.Model):
    Level_one = models.CharField(max_length=200)
    has_level_two=models.BooleanField(default=False)
    Level_two = models.CharField(max_length=200)
    has_level_three=models.BooleanField(default=False)
    Level_three = models.CharField(max_length=200)
    BriefDisription=RichTextField()
    Disription=RichTextField()
    Icon=models.ImageField(upload_to=generate_filename)
    created = models.DateTimeField(auto_now_add=True)

    objects = EntryQuerySet.as_manager()

    def __str__(self):
        return self.Level_one
    class Meta:
        verbose_name="Top Menu"
        verbose_name_plural="Top Menus"
        ordering=["-created"]
class menu_top_level(models.Model):
        Name = models.CharField(max_length=200)
        Order= models.IntegerField()
        url=models.URLField(max_length=200)
        published=models.BooleanField(default=False)
        created = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.Name
        class Meta:
            verbose_name="Top Menu"
            verbose_name_plural="Top Menus"
            ordering=["-Order"]

class menu_mid_level(models.Model):
        TopMenu = models.ForeignKey(menu_top_level, on_delete=models.CASCADE)
        Name = models.CharField(max_length=200)
        Order= models.IntegerField()
        url=models.URLField(max_length=200)
        published=models.BooleanField(default=False)
        created = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.Name

        class Meta:
            verbose_name="Mid Level Menu"
            verbose_name_plural="Mid Level Menus"
            ordering=["-Order"]

class menu_bot_level(models.Model):
        MiddleMenu = models.ForeignKey(menu_mid_level, on_delete=models.CASCADE)
        Name = models.CharField(max_length=200)
        Order= models.IntegerField()
        url=models.URLField(max_length=200)
        published=models.BooleanField(default=False)
        created = models.DateTimeField(auto_now_add=True)
        def __str__(self):
            return self.Name
        class Meta:
            verbose_name="Third Level Menu"
            verbose_name_plural="Third Level Menus"
            ordering=["-created"]

class Messages(models.Model):
    Name = models.CharField(max_length=200,error_messages={'blank' : 'BLANK','required' : 'REQUIRED'})
    Location = models.CharField(max_length=200)
    PhoneNumber=models.CharField( max_length= 15)
    Email= models.EmailField()
    Message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

class Pages(models.Model):
    Title = models.CharField(max_length=200)
    Descripton=RichTextField()
    published=models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name="Page"
        verbose_name_plural="Pages"

    def get_absolute_url(self):
                return "/kategori/%s/" % self.Title





