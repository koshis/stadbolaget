from companyapp.models import MenuItem

from . import models
import collections
from collections import OrderedDict

def menuitem(request):
    parentmenu=[]
    submenu1=[]
    result = []
    levelthreemenu=[]
    resultthirdlevel=[]
    finalmenu={}
    Category = models.menu_top_level.objects.all().order_by('Order')
    for menu in Category:
        print(menu.Name)
        parentmenu.append(menu.Name)
        submenu = models.menu_mid_level.objects.filter(TopMenu_id=menu.id).order_by('Order')
        if submenu.exists():
            for x in submenu:
                submenu1.append(x.Name)
                levelthree= models.menu_bot_level.objects.filter(MiddleMenu_id=x.id).order_by('Order')
                if levelthree.exists():
                    for x in levelthree:
                        print(levelthree)
                        levelthreemenu.append(x.Name)
                    resultthirdlevel.append(levelthreemenu)
                else:
                    resultthirdlevel.append('')

            result.append(submenu1)
            submenu1=[]
        else:
            result.append('')
        print(result)
        print(resultthirdlevel)
        finalmenu = OrderedDict(zip(parentmenu, result))
    return {'Category' : finalmenu}