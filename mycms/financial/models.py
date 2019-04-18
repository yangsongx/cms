from django.db import models
from django.utils import timezone

# Create your models here.
class Fund(models.Model):
    name = models.CharField(max_length=32, default='')
    fund_id = models.CharField(max_length=16, default='')
    description = models.CharField(max_length=128, default='')
    class Meta:
        verbose_name = '基金类型'
        verbose_name_plural = '基金类型'

    def __str__(self):
        return self.name

class Investment(models.Model):
    ENVIRONMENT = (
        (0, 'Gao'),
        (1, 'Yang'),
    )

    fund = models.ForeignKey(Fund, on_delete = models.CASCADE, blank=True, null=True)
    base_money =  models.FloatField(u'本金', default=0.0)
    who = models.IntegerField(u'投资人', choices=ENVIRONMENT, default=1)
    when = models.DateTimeField(blank=True, null=True, default=timezone.now)
    description = models.CharField(max_length=128, default='')
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = '投资记录'
        verbose_name_plural = '投资记录'

class Outcoming(models.Model):
    ENVIRONMENT = (
        (0, 'Gao'),
        (1, 'Yang'),
    )
    fund = models.ForeignKey(Fund, on_delete = models.CASCADE, blank=True, null=True)
    base_money =  models.FloatField(default=0.0)
    who = models.IntegerField(u'撤资人', choices=ENVIRONMENT, default=1)
    when = models.DateTimeField(blank=True, null=True, default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = '出资记录'
        verbose_name_plural = '出资记录'

class MoneyDetails(models.Model):
    fund = models.ForeignKey(Fund, on_delete = models.CASCADE, blank=True, null=True)
    price =  models.FloatField(default=0.0)
    count = models.FloatField(default=0.0)

# FIXME - this aims to be used to override standard admin framewrok..
class Summary(models.Model):
    class Meta:
        verbose_name = '财富一览'
        verbose_name_plural = '财富一览'
    pass
