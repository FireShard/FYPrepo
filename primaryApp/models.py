from django.db import models

# Create your models here.
class RamDetails(models.Model):
    ramid = models.AutoField(primary_key=True)
    manufacturer = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    ramType = models.CharField(max_length=255)
    ramSize = models.CharField(max_length=255)
    ramLink = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.ramSize} {self.ramType}"

class LaptopDetails(models.Model):
    laptopid = models.AutoField(primary_key=True)
    manufacturer = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    productLine = models.CharField(max_length=255)
    CPU = models.CharField(max_length=255)
    ramSize = models.CharField(max_length=255)  
    ramType = models.CharField(max_length=255)  

    def __str__(self):
        return f"{self.brand} {self.productLine}"

class UserLaptop(models.Model):
    userid = models.AutoField(primary_key=True)
    manufacturer = models.CharField(max_length=255)
    ramSize = models.IntegerField()
    architecture = models.IntegerField()
    CPUbrand = models.CharField(max_length=255)
    CPUName = models.CharField(max_length=255)
    CPUGen = models.CharField(max_length=255)
    ramType = models.CharField(max_length=255)
    ram = models.ForeignKey(RamDetails, on_delete=models.SET_NULL, null=True, blank=True, related_name='user_laptops')
    laptop = models.ForeignKey(LaptopDetails, on_delete=models.CASCADE, related_name='user_laptops')

    def __str__(self):
        return f"User Laptop: {self.laptop}"