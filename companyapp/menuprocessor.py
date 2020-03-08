from companyapp.models import MenuItem

from . import models
import collections
from collections import OrderedDict

def findsubmenu(name):
    menus=[]
    submenu=models.Menucategory.objects.filter(menu__menu=name)
    for x in submenu:
        menus.append(x)
    return menus
    
def menuitem(request):
    menu={}
    mainmenu=models.MenuItem.objects.filter(published=True)
    for x in mainmenu:
        menu[x]=findsubmenu(x.menu)
    return{ 'Category':menu}
