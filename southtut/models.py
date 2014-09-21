from django.db import models
import fields

class Knight(models.Model):
    name = models.CharField(max_length=100, unique=True)
    of_the_round_table = models.BooleanField()
    dances_whenever_able = models.BooleanField()
    shrubberies = models.IntegerField(null=False)

class Group(models.Model):
    name = models.CharField(max_length=144, verbose_name="Name")
    facebook_page_id = models.CharField(max_length=255)
    tags = fields.TagField(default=[])
    ups = fields.UpperCaseField(default="")
