from __future__ import unicode_literals

from django.db import models

# Create your models here.

# Create your models here.
from django.contrib import admin # 加上這個才可以管理

    
class Lotus(models.Model): #法华经
    ## auto primary_key
    id = models.AutoField(primary_key=True) ## 层次
    level = models.IntegerField() ## 层次
    parent = models.IntegerField() ## 父节点
    code  = models.CharField(max_length=64, blank=True, null=True) ## 编码
    sanskrit = models.CharField(max_length=8192, blank=True, null=True) ## 梵語
    sanskrit_eq = models.CharField(max_length=8192, blank=True, null=True) ## 梵语原型
    tag = models.CharField(max_length=8192, blank=True, null=True) ## 注
    chinese_explain = models.CharField(max_length=8192, blank=True, null=True) ## 现代汉译
    note = models.CharField(max_length=8192, blank=True, null=True) ## 注
    d = models.CharField(max_length=8192, blank=True, null=True) ## 
    k = models.CharField(max_length=8192, blank=True, null=True) ## 
    dnote = models.CharField(max_length=8192, blank=True, null=True) ##  翻译的说明
    knote = models.CharField(max_length=8192, blank=True, null=True) ##  翻译的说明
    
admin.site.register(Lotus)