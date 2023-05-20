from django.contrib import admin
from .models import *


class Background_imgAdmin(admin.ModelAdmin):
    pass

class intro_imgAdmin(admin.ModelAdmin):
    pass  # Add any customizations or additional fields you want to display

class Product1Admin(admin.ModelAdmin):
    pass

class Product2Admin(admin.ModelAdmin):
    pass

class Product3Admin(admin.ModelAdmin):
    pass

class AbutusAdmin(admin.ModelAdmin):
    pass



admin.site.register(Company)
admin.site.register(Background_img, Background_imgAdmin)
admin.site.register(intro_img, intro_imgAdmin)
admin.site.register(product1, Product1Admin)
admin.site.register(product2, Product2Admin)
admin.site.register(product3, Product3Admin)
admin.site.register(Aboutus, AbutusAdmin)
admin.site.register(FacebookLink)
admin.site.register(LinkedinLink)

