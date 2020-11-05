from django.contrib import admin
from .models import Settings, Experince, Education, Skills, Skills_tools, Awards

admin.site.register(Settings)

admin.site.register(Experince)

admin.site.register(Education)

admin.site.register(Skills_tools)

admin.site.register(Skills)


admin.site.register(Awards)
