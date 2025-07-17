from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Medicine, UserMedicine, Supplier, Reminder, IntakeLog

admin.site.register(User, UserAdmin)
admin.site.register(Medicine)
admin.site.register(UserMedicine)
admin.site.register(Supplier)
admin.site.register(Reminder)
admin.site.register(IntakeLog)
