from django.db import models
from django.contrib import admin
class vehicle_DB(models.Model):
    Service_no=models.IntegerField()
    Customer_Name=models.CharField(max_length=20)
    Bike_Models=models.CharField(max_length=20)
    Service_Date=models.DateField()
    Service_Cost=models.FloatField()
    Address=models.TextField()
    Service_Type=models.CharField(max_length=30)

class vehicle_DBAdmin(admin.ModelAdmin):
    list_display=["Customer_Name","Bike_Models","Service_no"]