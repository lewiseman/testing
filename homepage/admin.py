from django.contrib import admin
from .models import *

admin.site.site_header = 'Indulge.me'

admin.site.register(Hadithi)
admin.site.register(MainTag)
admin.site.register(SubTag)
admin.site.register(DemoStories)