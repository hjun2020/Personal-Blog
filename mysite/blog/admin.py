from django.contrib import admin
from blog.models import AccessRecord, Topic, Webpage, Posting, User
# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(Posting)
admin.site.register(User)
