from django.contrib import admin
from .models import MenuItem,Menucategory, Messages
from markdownx.admin import MarkdownxModelAdmin
from django_markdown.admin import MarkdownModelAdmin

admin.site.site_header = 'Städbolaget'

class MessagesAdmin(MarkdownxModelAdmin):
    list_display=("Name","Email","Location","created")

class TopMenu(MarkdownxModelAdmin):
    list_display=("menu","order","url","created","published")

class submenu(MarkdownModelAdmin):
    list_display=("name","order","url","created","published")

admin.site.register(MenuItem, TopMenu)
admin.site.register(Menucategory, submenu)

admin.site.register(Messages, MessagesAdmin)






# Register your models here.
