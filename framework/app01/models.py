from __future__ import unicode_literals
from django.db import models

# Create your models here.

class TServer(models.Model):
    app = models.CharField(primary_key=True, max_length=64)
    server = models.CharField(max_length=64)
    division = models.CharField(max_length=64)
    node = models.CharField(max_length=64)
    status = models.IntegerField()
    use_agent = models.IntegerField()

    class Meta:
        managed = True
        db_table = 't_server'
        unique_together = (('app', 'server', 'division', 'node'),)


class TService(models.Model):
    app = models.CharField(primary_key=True, max_length=64)
    server = models.CharField(max_length=64)
    division = models.CharField(max_length=64)
    node = models.CharField(max_length=64)
    service = models.CharField(max_length=128)
    endpoint = models.CharField(max_length=512)

    class Meta:
        managed = True
        db_table = 't_service'
        unique_together = (('app', 'server', 'division', 'node', 'service'),)
