from django.db import models

class TodosModel(models.Model):
    td = models.CharField(max_length=200,default=0)
