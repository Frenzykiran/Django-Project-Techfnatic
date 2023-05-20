from django.contrib import admin
from django.shortcuts import render
from .models import *


#Django Admin customisation

admin.site.site_header = "Admin | TechFnatic"
admin.site.site_title = "TechFnatic Admin"
admin.site.index_title = "Welcome to Admin Portal"

# Create your views here.
def index(request):
    companyName = Company.objects.first()
    backimage = Background_img.objects.first()  # Assuming you have only one configuration object
    intro_img_obj = intro_img.objects.first()
    product1_img = product1.objects.first()
    product2_img = product2.objects.first()
    product3_img = product3.objects.first()
    Aboutus_img = Aboutus.objects.first()
    Facebook_link = FacebookLink.objects.first()
    Linkedin_Link = LinkedinLink.objects.first()
    context = {
        'companyName': companyName.c_name if companyName else None,
        'backimage': backimage,
        'intro_img': intro_img_obj,
        'product1_img' : product1_img,
        'product2_img' : product2_img,
        'product3_img' : product3_img,
        'Aboutus_img' : Aboutus_img,
        'Facebook_link': Facebook_link,
        'Linkedin_Link': Linkedin_Link,
    }
    return render(request, 'index.html', context)




