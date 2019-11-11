from django.contrib import admin
from .models import TimeInterval, Status, RepeatAmount

admin.site.register(TimeInterval)
admin.site.register(Status)
admin.site.register(RepeatAmount)
