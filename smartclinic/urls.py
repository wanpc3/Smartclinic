from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from clinic.views import *

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'medicines', MedicineViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'usermedicines', UserMedicineViewSet)
router.register(r'reminders', ReminderViewSet)
router.register(r'intakelogs', IntakeLogViewSet)

urlpatterns = [
    path('', include('clinic.urls')),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
