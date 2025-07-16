from rest_framework import serializers
from .models import User, Medicine, Supplier, UserMedicine, Reminder, IntakeLog

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class UserMedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMedicine
        fields = '__all__'

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = '__all__'

class IntakeLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntakeLog
        fields = '__all__'