from django.contrib import admin
from .models import MenuItem, menu_top_level,menu_mid_level,menu_bot_level,Messages, Pages
from markdownx.admin import MarkdownxModelAdmin
from django_markdown.admin import MarkdownModelAdmin

admin.site.site_header = 'Städbolaget'

class MessagesAdmin(MarkdownxModelAdmin):
    list_display=("Name","Email","Location","created")

class TopMenu(MarkdownxModelAdmin):
    list_display=("Name","Order","url","published")

class Page(MarkdownModelAdmin):
    list_display=("Title","published")

admin.site.register(MenuItem, MarkdownxModelAdmin)
admin.site.register(menu_top_level, TopMenu)
admin.site.register(menu_mid_level, MarkdownxModelAdmin)
admin.site.register(menu_bot_level, MarkdownxModelAdmin)
admin.site.register(Messages, MessagesAdmin)
admin.site.register(Pages, Page)






# Register your models here.
