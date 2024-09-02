from django.db import models

# Create your models here.
class newModel(models.Model):
    name = models.CharField(("Your Name"), max_length=50)
    '''
    create table newModel(name);
    '''