from django.contrib import admin

from .models import User
from .models import News
from .models import NewsCategory

admin.site.register(User)
admin.site.register(News)
admin.site.register(NewsCategory)