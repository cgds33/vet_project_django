from django.db import models

# Create your models here.

class Pet(models.Model):
    # Pet Model Fields
    # Pet model has defined for pet postings
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Animal Lover")
    petName = models.CharField(max_length=50,verbose_name="Pet Name")
    petType = models.CharField(max_length=50,verbose_name="Pet Type")
    petSpecies = models.CharField(max_length=50,verbose_name="Pet Species")
    petAge = models.CharField(max_length=50,verbose_name="Pet Age")
    content = models.TextField(verbose_name="Detail")
    createdDate = models.DateTimeField(auto_now_add=True,verbose_name="Created Date")
    petImage = models.FileField(blank = True,null=True,verbose_name="Add pet's image..")

    def __str__(self):
        return self.petName


