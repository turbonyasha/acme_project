from django.contrib import admin

from .models import Tag, Birthday, Congratulation

admin.site.register(Tag)
admin.site.register(Birthday)
admin.site.register(Congratulation)
