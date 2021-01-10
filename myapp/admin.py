from django.contrib import admin
from .models import Measurement
# Register your models here.
@admin.register(Measurement)

class AdminMeasument(admin.ModelAdmin):
    model = Measurement
    list_display = ['location','destination','distance']