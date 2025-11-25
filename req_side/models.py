from django.db import models

class Member (models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    amount = models.IntegerField()
    
class Per (models.Model):
    usn = models.CharField(max_length=20)
    psw = models.CharField(max_length=20)

