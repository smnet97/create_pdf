from django.db import models


class LogoModel(models.Model):
    logo = models.ImageField(upload_to='logo/')


