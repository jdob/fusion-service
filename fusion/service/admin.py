from django.contrib import admin

from .models import (Category, Partner, PartnerCategory)

# Register your models here.
admin.site.register(Category)
admin.site.register(Partner)
admin.site.register(PartnerCategory)